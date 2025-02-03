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

For a detailed evaluation of the model, including additional analysis and visualizations, refer to the [evaluation notebook](https://github.com/julsCadenas/summarize-reddit/blob/master/notebooks/eval.ipynb).

## **BERTScore**

The model’s performance was evaluated using **BERTScore** (Precision, Recall, and F1).

### **Average BERTScores**  
| Metric              | Value     |
|---------------------|-----------|
| **Precision (p)**| 0.8704    |
| **Recall (r)**   | 0.8517    |
| **F1 Score (f)** | 0.8609    |

### **Conclusion**
- **Precision** is strong but can be improved by reducing irrelevant tokens.
- **Recall** needs improvement to capture more relevant content.
- **F1 Score** indicates a solid overall performance.

### **Improvements**
- Focus on improving **Recall**.
- Perform **Error Analysis** to identify missed content.
- **Fine-tune** the model for better results.

## **ROUGE**

The following table summarizes the ROUGE scores (Recall, Precision, and F1) for three different metrics: ROUGE-1, ROUGE-2, and ROUGE-L. These values represent the mean scores across all summaries.

### **Average ROUGE Scores**  
| Metric       | ROUGE-1   | ROUGE-2   | ROUGE-L   |
|--------------|-----------|-----------|-----------|
| **Recall (r)** | 32.20     | 7.10      | 30.09     |
| **Precision (p)** | 22.03   | 4.90      | 20.50     |
| **F1 Score (f)**  | 25.00   | 5.51      | 23.30     |

### **Interpretation**
- **ROUGE-1**: Shows higher recall and precision, indicating that the model is good at capturing single-word overlaps but could reduce irrelevant words.
- **ROUGE-2**: Exhibits lower recall and precision, indicating the model struggles with bigram relationships and context.
- **ROUGE-L**: Performs better than ROUGE-2 but still faces challenges with precision. It captures longer subsequences more effectively than bigrams.

## **Conclusion**
- **ROUGE-1**: The model shows moderate performance but generates some irrelevant words (low precision).
- **ROUGE-2**: The model performs poorly, indicating difficulty in capturing bigram relationships.
- **ROUGE-L**: Slightly better than ROUGE-2, with some success in capturing longer sequences.

## **Improvements**
- Focus on enhancing **bigram overlap** (ROUGE-2) and overall **context understanding**.
- Reduce **irrelevant content** for improved **precision**.
- Improve **sequence coherence** for better **ROUGE-L** scores.
