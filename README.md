# OpenAI Task

A Python application that uses OpenAI's API to generate HTML markups based on a given input text articles.

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yurenianastya/openai_task.git
    cd openai_task
    ```

2. Install dependencies using `pip` or `conda`:

    - **With `pip`**:

      ```bash
      pip install -r requirements.txt
      ```

    - **With `conda`** (if you prefer using Conda environments):

      ```bash
      conda create --name openai_task_env python=3.8
      conda activate openai_task_env
      pip install -r requirements.txt
      ```

3. Set up your environment variables for OpenAI API credentials:

    - Create a `.env` file in the project root and add your OpenAI API key:
      ```
      OPENAI_API_KEY=your-api-key-here
      ```

## Usage

2. Once you have the environment set up, add your text file with the article to the project. Rename it to ```input.txt``` or change in ```main.py``` the ```input_file``` value to your desire

2. Run the main script:

    ```bash
    python main.py
    ```
    If everything goes well, you can find the script's output in ```artykul.html```
