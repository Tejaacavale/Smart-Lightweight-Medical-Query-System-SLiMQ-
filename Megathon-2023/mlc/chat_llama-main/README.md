# README

## Model From

* The repository uses the 4 bit quantized **Llama 2 7B Chat GPTQ** model.

* Model credits - https://huggingface.co/TheBloke/Llama-2-7b-Chat-GPTQ
* License: As mentioned in the [original HuggingFace repository](https://huggingface.co/TheBloke/Llama-2-7b-Chat-GPTQ#original-model-card-metas-llama-2-7b-chat).

## Steps to Run

* Clone this repository

```
git clone https://github.com/sovit-123/chat_llama.git
```

```
cd chat_llama
```

* Install requirements

```
pip install -r requirements.txt
```

* Clone the **LLama 2 7b Chat GPTQ** repository so that the model stays in the local folder instead of cache. They are quite huge.

```
git clone https://huggingface.co/TheBloke/Llama-2-7b-Chat-GPTQ
```

* Run

```
python run.py --prompt "python function to add two numbers"
```

The output:

````
Great! I'm happy to help you with your Python function. To add two numbers in Python, you can use the `+` operator. Here's an example:
```
def add_numbers(num1, num2):
    return num1 + num2

# Example usage
result = add_numbers(3, 5)
print(result) # Output: 8
```
````

## Advanced Prompting (All results from a 10 GB RTX 3080 GPU)

Suppose that you have some content in the `prompt.txt` file. A sample file is already provided with the repository. This contains a part of the DETR paper. You can replace it with your own content. Here are some prompting techniques:

* Instead of a prompt, provide the text file path and set the agenda as `summarize`:

```
python run.py --prompt data/prompt.txt --system-agenda "summarize"
```

Output:

```
Summary:
The paper presents a new method for object detection called DEtection TRansformer (DETR). DETR views object detection as a direct set prediction problem, eliminating the need for hand-designed components like non-maximum suppression or anchor generation. DETR uses a transformer encoder-decoder architecture and a set-based global loss to force unique predictions via bipartite matching. The model directly predicts the final set of detections in parallel, without requiring specialized libraries or post-processing steps. DETR demonstrates accuracy and runtime performance on par with the well-established and highly-optimized Faster R-CNN baseline on the challenging COCO object detection dataset. Additionally, DETR can be easily generalized to produce panoptic segmentation in a unified manner. The paper shows that DETR significantly outperforms competitive baselines and provides insights into the design choices that contribute to its success.
```

* The text file can be quite large and prompting the entire content to the model can result in CUDA OOM. By default the script considers only the first 11000 characters. We can increase or decrease the limit using the `--limit` argument. Higher limit gives better outputs. Set `--limit -1` to consider the all the content of the file.
  * Following is an example to do so. No output shown as I get CUDA OOM on 10 GB GPU.

```
python run.py --prompt data/prompt.txt --system-agenda "summarize" --limit -1
```

* By default the model generates 512 new tokens. We can set the number of tokens using `--new-tokens`

```
python run.py --prompt data/prompt.txt --system-agenda "summarize in 1000 words" --new-tokens 2048
```

Output:

```
Summary: End-to-End Object Detection with Transformers
The paper presents a new method for object detection that views it as a direct set prediction problem. The proposed method, called DEtection TRansformer (DETR), uses a transformer encoder-decoder architecture and a set-based global loss to directly predict the final set of detections without the need for manual feature engineering or post-processing steps. DETR demonstrates accuracy and runtime performance on par with the well-established and highly-optimized Faster R-CNN baseline on the challenging COCO object detection dataset. Additionally, DETR can be easily generalized to produce panoptic segmentation, a related task that involves assigning semantic labels to pixels in an image.
Key contributions:
* Proposes a new method for object detection that views it as a direct set prediction problem.
* Introduces a transformer encoder-decoder architecture and a set-based global loss to directly predict the final set of detections.
* Demonstrates equality of performance with the well-established and highly-optimized Faster R-CNN baseline on the challenging COCO object detection dataset.
* Shows that DETR can be easily generalized to produce panoptic segmentation, a related task that involves assigning semantic labels to pixels in an image.
* Provides a detailed analysis of the components of the DETR model and their impact on performance.
```

