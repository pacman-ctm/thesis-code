# Thesis of Pham Anh Cuong  
This is the source code that is used in the graduation thesis of Pham Anh Cuong (ID 19020038) of VNU University of Engineering and Technology for 2023 Spring Semester.

### About the folders:

- Data_making: About the code for creating image captioning dataset. 
- Train: About the training phase code.
- Inference: About the inference phase code (usually after getting the snapshot after the training phase).
- Eval: About the evaluation phase of the models.

### About the models:
For my graduation thesis, I use three models with its architecture as follows:
- Model using **ResNet101** for feature extracting and **LSTM** for caption generating.
- Model using **Vision Transformer** for feature extracting and **Transformer Decoder** for caption generating.
- Model-based on the **GRIT** model [Arxiv](https://arxiv.org/abs/2207.09666), however, due to the lack of hardware condition, the code for this modification is available at the [vicap branch](https://github.com/davidnvq/grit/tree/vicap) in the source code repository of GRIT.