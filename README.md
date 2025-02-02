# **Reddit Summarization Model**

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

<br>

# **Model Evaluation**

## **ROUGE**

| Metric    | Recall (%) | Precision (%) | F1-Score (%) |
|-----------|------------|---------------|--------------|
| **ROUGE-1** | 57.66      | 43.41         | 49.53        |
| **ROUGE-2** | 29.30      | 20.72         | 24.27        |
| **ROUGE-L** | 56.20      | 42.30         | 48.28        |


### **CONCLUSIONS**
**ROGUE-1 SCORE:** The ROUGE-1 score indicates that the model is fairly good at capturing individual words (unigrams) from the reference summaries. With a recall of 57.66%, the model captures more than half of the relevant words from the reference summaries, which suggests that it's effectively capturing key content. The precision of 43.41% indicates that a significant portion of the generated summary’s words also appear in the reference, but there may be some additional, irrelevant words included. The F1-score of 49.53% shows that, overall, there’s a fairly good balance between recall and precision, although there's still room to increase both aspects for better results.

**ROGUE-2 SCORE:** The ROUGE-2 score, which focuses on bigram overlap, is considerably lower than ROUGE-1. The recall of 29.30% indicates that the model captures roughly 30% of the bigrams from the reference summaries, which is a moderate result but suggests that the model may not be fully preserving the structural relationships between words. The precision of 20.72% suggests that the generated summaries might include bigrams that are not present in the reference summaries. The F1-score of 24.27% is relatively low, which may indicate that the model needs improvement in capturing bigram patterns in the summaries. This is common in summarization tasks, as producing high-quality bigram overlap is challenging.

**ROGUE-l SCORE:** The ROUGE-L score, which focuses on the longest common subsequence (LCS), shows that the model is able to capture the overall structure of the reference summaries quite well. The recall of 56.20% suggests that a large portion of the key sequences (order-preserving) from the reference summaries appear in the generated summaries, indicating good coherence. The precision of 42.30% shows that the model does well in maintaining relevant sequences in the generated summary but could further reduce redundant or non-informative sequences. The F1-score of 48.28% indicates a solid performance in preserving the flow and structure of the original text.

### **SUMMARY**  
- The ROUGE-1 score is strong, indicating that the model is capturing individual words well, which is important for summarizing the key points of Reddit posts. This suggests the model is effectively identifying the core content from the original Reddit discussions.

- The ROUGE-2 score is relatively low, suggesting that the model struggles with preserving the structure and sequence of words, which is crucial for generating coherent summaries of Reddit posts where sentence flow and the connection between ideas are important.

- The ROUGE-L score shows that the model is effectively capturing meaningful sequences and maintaining coherence in the summaries. This is a positive outcome for summarizing Reddit posts, where keeping the overall message and flow intact is important.

While the model performs well in certain areas (particularly with ROUGE-1 and ROUGE-L), there is room for improvement, especially with the ROUGE-2 score. Improving bigram overlap could enhance the fluency and structure of the summaries, leading to more readable and coherent summaries of Reddit posts.

## **BERTScore**

| Metric    | Value (%) |
|-----------|-----------|
| **Recall**    | 90.85     |
| **Precision** | 92.44     |
| **F1-Score**  | 91.64     |

#### **Notes:**
- Some weights of RobertaModel were not initialized from the model checkpoint at roberta-large and are newly initialized, which might lead to the model not performing optimally until it is trained further.

### **CONCLUSIONS**

- **Precision (P):** 0.9085, meaning that 90.85% of the words in the generated summaries are also present in the reference summaries. This indicates that the generated summaries are highly precise, with a minimal amount of irrelevant information.

- **Recall (R):** 0.9244, meaning that 92.44% of the words in the reference summaries are also found in the generated summaries. This suggests that the model is capturing the majority of the essential information from the reference summaries.

- **F1 score:** 0.9164, which is the harmonic mean of Precision and Recall. This score balances both Precision and Recall, indicating that the model performs well in generating summaries that are both accurate (Precision) and comprehensive (Recall).

### **SUMMARY** 
- The high **F1 score** shows that the model is effectively summarizing the content by maintaining a balance between including relevant information and avoiding unnecessary or irrelevant details.

- The **Precision** and **Recall** values suggest that the model is capturing a substantial portion of the content while keeping the information concise and relevant. The performance is impressive, even considering that some model weights were randomly initialized during the evaluation.

- While the model performs well, further fine-tuning, especially for the pooler layer, might lead to slight improvements in semantic understanding and overall summary quality.

