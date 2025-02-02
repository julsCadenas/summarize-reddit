# Reddit Summarization Model

This project uses a fine-tuned model for summarizing Reddit posts and their comments. The model has been trained using a dataset of 100 Reddit posts, and the goal is to generate concise and meaningful summaries of the original posts and the associated comments.

## Model on Hugging Face

This project uses a fine-tuned version of the BART model from Facebook for summarizing Reddit posts and their comments. The original model, facebook/bart-large-cnn, is a pre-trained sequence-to-sequence model optimized for summarization tasks. It was fine-tuned on a custom Reddit dataset for this project.

- **Original Model:** [facebook/bart-large-cnn](https://huggingface.co/facebook/bart-large-cnn)
- **Fine-Tuned Model:** [julsCadenas/summarize-reddit](https://huggingface.co/julsCadenas/summarize-reddit)

## Installation

To get started, you need to install the required dependencies. You can do this by creating a virtual environment and installing the packages listed in `requirements.txt`.

### **Steps:**

1. Clone the repository:
   ```bash
    git clone https://github.com/your-username/reddit-summarizer.git
    cd reddit-summarizer  
2. Set up a virtual environment:
   ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows, use 'venv\Scripts\activate'  
2. Install depdendencies:
   ```bash
    pip install -r requirements.txt  
3. Set up your environment variables (if needed) by creating a ```.env``` file. You can refer to the sample ```.env.example``` for the necessary variables.

### **Usage**

1. In ```src/summarize.py```, the model should be initialized like this:
    ```python
      # src/summarize.py
      self.summarizer = pipeline(
        "summarization",
        model = "julsCadenas/summarize-reddit",
        tokenizer = "julsCadenas/summarize-reddit",
      )   
2. Add the *URL* of your preferred Reddit post on main.py.
3. Run ```src/main.py```

## **Model Evaluation**

### **ROGUE-1 SCORES:**
- **Recall (r)** = 57.66%
- **Precision (p)** = 43.41%
- **F1-Score (f)** = 49.53%

### **ROUGE-2 SCORES:**
- **Recall (r)** = 29.30%
- **Precision (p)** = 20.72%
- **F1-Score (f)** = 24.27%

### **ROUGE-L SCORES:**
- **Recall (r)** = 56.20%
- **Precision (p)** = 42.30%
- **F1-Score (f)** = 48.28%

<br>

**ROUGE-1:** also known as unigram, measures the overlap of unigrams (individual words) between the generated summary and the reference summary. It calculates the proportion of words in the generated summary that are also present in the reference summary. Example: Reference text: “The cat is on the rug” Generated text: “The dog is on the rug” ROUGE-1 = 3/5 = 0.6.

**ROUGE-2:** also known as bigram, measures the overlap of bigrams (pairs of consecutive words) between the generated summary and the reference summary. It calculates the proportion of bigrams in the generated summary that are also present in the reference summary.

**ROUGE-L:** measures the similarity between the word sequence of the generated abstract and the reference abstract using the longest sequence of words in common. Unlike ROUGE-1 and ROUGE-2, which use a simple word count approach, ROUGE-L uses a string matching approach.

**Source:** https://fabianofalcao.medium.com/metrics-for-evaluating-summarization-of-texts-performed-by-transformers-how-to-evaluate-the-b3ce68a309c3

### **CONCLUSIONS**
**ROGUE-1 SCORE:** The ROUGE-1 score indicates that the model is fairly good at capturing individual words (unigrams) from the reference summaries. With a recall of 57.66%, the model captures more than half of the relevant words from the reference summaries, which suggests that it's effectively capturing key content. The precision of 43.41% indicates that a significant portion of the generated summary’s words also appear in the reference, but there may be some additional, irrelevant words included. The F1-score of 49.53% shows that, overall, there’s a fairly good balance between recall and precision, although there's still room to increase both aspects for better results.

**ROGUE-2 SCORE:** The ROUGE-2 score, which focuses on bigram overlap, is considerably lower than ROUGE-1. The recall of 29.30% indicates that the model captures roughly 30% of the bigrams from the reference summaries, which is a moderate result but suggests that the model may not be fully preserving the structural relationships between words. The precision of 20.72% suggests that the generated summaries might include bigrams that are not present in the reference summaries. The F1-score of 24.27% is relatively low, which may indicate that the model needs improvement in capturing bigram patterns in the summaries. This is common in summarization tasks, as producing high-quality bigram overlap is challenging.

**ROGUE-l SCORE:** The ROUGE-L score, which focuses on the longest common subsequence (LCS), shows that the model is able to capture the overall structure of the reference summaries quite well. The recall of 56.20% suggests that a large portion of the key sequences (order-preserving) from the reference summaries appear in the generated summaries, indicating good coherence. The precision of 42.30% shows that the model does well in maintaining relevant sequences in the generated summary but could further reduce redundant or non-informative sequences. The F1-score of 48.28% indicates a solid performance in preserving the flow and structure of the original text.

### **SUMMARY**  
- The ROUGE-1 score is strong, indicating that the model is capturing individual words well, which is important for summarizing the key points of Reddit posts. This suggests the model is effectively identifying the core content from the original Reddit discussions.

- The ROUGE-2 score is relatively low, suggesting that the model struggles with preserving the structure and sequence of words, which is crucial for generating coherent summaries of Reddit posts where sentence flow and the connection between ideas are important.

- The ROUGE-L score shows that the model is effectively capturing meaningful sequences and maintaining coherence in the summaries. This is a positive outcome for summarizing Reddit posts, where keeping the overall message and flow intact is important.

While the model performs well in certain areas (particularly with ROUGE-1 and ROUGE-L), there is room for improvement, especially with the ROUGE-2 score. Improving bigram overlap could enhance the fluency and structure of the summaries, leading to more readable and coherent summaries of Reddit posts.

