import click
from transformers import pipeline
import urllib.request
from bs4 import BeautifulSoup
import os

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'

# Function to extract text from the URL
def extract_from_url(url):
    text = ""
    req = urllib.request.Request(url, data=None, headers={
        'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36"
    })
    html = urllib.request.urlopen(req)
    parser = BeautifulSoup(html, 'html.parser')
    # Extract all paragraphs' text
    for paragraph in parser.find_all("p"):
        text += paragraph.text
    return text

# Function to summarize the text
def process(text):
    summarizer = pipeline("summarization", model="t5-small")
    # Split text into chunks if it's too long
    max_input_length = 512  # Model input size limit in tokens
    input_chunks = [text[i:i+max_input_length] for i in range(0, len(text), max_input_length)]
    input_chunks = input_chunks[:2]
    
    summaries = []
    for chunk in input_chunks:
        result = summarizer(chunk, max_length=180, min_length=30, do_sample=False)
        summaries.append(result[0]['summary_text'])
    
    click.echo("Summarization process complete")
    click.echo("=" * 50)
    return " ".join(summaries)

# Correct the decorator name
@click.command()
@click.option('--url', help="URL of the webpage to summarize.")
@click.option('--file', help="Local file to summarize.")
def main(url, file):
    text = ""
    if url:
        text = extract_from_url(url)
    elif file:
        with open(file, 'r') as _f:
            text = _f.read()
    else:
        click.echo("Please provide either a URL or a file.")

    click.echo(f"Summarized text from -> {url or file}")
    click.echo(process(text))

if __name__ == '__main__':
    main()
