# Project-3
RAG Application Using Llama-3


## Overview

This RAG Application provides a comprehensive approach to reading and processing PDF and TXT files using advanced NLP models and libraries. It integrates multiple tools to facilitate the extraction and manipulation of text data, with additional capabilities for Slack integration.

### Table of Contents

- [Overview](#overview)
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Integration with Slack](#integration-with-slack)
- [Contributing](#contributing)
- [License](#license)

### Overview

The `llama_pdf_reader_v4.ipynb` RAG Application is designed for:

- **Reading and Processing PDF/TXT Files**: Utilizing custom readers and embedding models to process large sets of documents.
- **NLP Tasks with LLaMA**: Implementing LLaMA, a powerful large language model, for natural language processing tasks.
- **Slack Integration**: Interacting with Slack using `slack_sdk` and `slack_bolt` for seamless notifications and data sharing.

### Installation

To run this RAG Application, you need to install the following Python libraries:

```bash
pip install chromadb llama_index slack_sdk slack_bolt flask python-dotenv
```

Ensure you also have access to the necessary NLP models and embeddings, such as HuggingFace models.

### Usage

1. **Set Up Directories**: Define the directories for your PDF and TXT files.
   ```python
   pdf_folder_path = '/path/to/your/pdf/folder/'
   txt_folder_path = '/path/to/your/txt/folder/'
   ```
   
2. **Initialize the LLaMA Model**: Set up the LLaMA model for NLP tasks.
   ```python
   llm = Ollama(model="llama3")
   ```

3. **Run the RAG Application**: Execute the cells in the RAG Application to process documents and interact with Slack.

### Features

- **PDF and TXT File Processing**: Read and process documents in different formats using custom readers.
- **NLP with LLaMA**: Perform advanced NLP tasks using LLaMA models.
- **Slack Notifications**: Send and receive notifications or data through Slack.

### Integration with Slack

To use Slack integration, set up your Slack App and obtain the required tokens and credentials. Update the `.env` file with your Slack credentials.

```bash
SLACK_BOT_TOKEN=xoxb-your-slack-bot-token
SLACK_APP_TOKEN=xapp-your-slack-app-token
```

### Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

### Author
This code was written by [Richard Lankford](https://github.com/rwlankford/Project-3) with assistance and review from **Rimi Sharma** and **Tyler B. Shubert**

### License

This project is licensed under the MIT License.

Copyright (c) 2024 SlackAPI

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
