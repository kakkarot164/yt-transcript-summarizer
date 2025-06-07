#🎥 YT Transcript Summarizer

Extract transcripts from YouTube videos and generate concise summaries using state-of-the-art NLP models like BART, T5, and Pegasus.


##✅ Features

**📹 YouTube Transcript Extraction – Automatically fetch transcripts from YouTube videos.

**🧠 Summarization using multiple models – Supports fine-tuned models like BART, T5, and Pegasus.

**📈 Sentence similarity & readability scoring – Assess the coherence and readability of generated summaries.

**🗣️ Speech-to-text fallback – Handles cases where captions are unavailable.

**💾 Save results in text/JSON – Export summaries for further use.

**🧪 Experiment logging – Track trials and evaluation in trials.ipynb.


📁 Project Structure

YT_transcript_summarizer/

├── app.py Main application file

├── main.py Entry point for execution

├── requirements.txt Dependencies list

├── setup.py Package setup configuration

├── runtime.txt Runtime specifications

├── Procfile Deployment configuration

├── README.md Project documentation

├── .gitignore Git ignored files

├── .gitattributes Git attributes

│ ├── research/ Research experiments & notebooks

│ └── trials.ipynb

│ ├── assets/ Static assets directory

│ └── .gitkeep

│ └── src/ Source code folder

└── YT_transcript_summarizer/

├── init.py │ ├── config/ │ Configuration files │ └── config.yaml │ ├── logging/ │ Logging setup │ └── init.py │ ├── pipeline/ │ Summarization pipeline │ ├── init.py │ └── summary_pipeline.py │ ├── utils/ │ Utility functions │ ├── init.py │ └── common.py  

##🚀 Getting Started

###Clone the repository

git clone https://github.com/kakkarot164/yt-transcript-summarizer.git

cd yt-transcript-summarizer

###Install dependencies

pip install -r requirements.txt

###Run the application

python main.py


##🤖 Models Used

The following pre-trained NLP models are utilized for text summarization:

facebook/bart-large-cnn

t5-small

google/pegasus-xsum

##📜 License

This project is licensed under the MIT License. See the LICENSE file for more details.