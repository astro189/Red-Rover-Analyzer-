# Red-Rover-Analyzer-
## Color-Based Primary Segmentation

The Mars Rover AI employs a color-based segmentation approach to perform primary segmentation of the Martian soil. The following steps outline the process:

1. **Histogram Equalization:** Utilizing CLAHE to enhance image quality by addressing overexposure.

   - Before Histogram Equalization | After Histogram Equalization
     --- | ---
     ![Picture1](https://github.com/astro189/Red-Rover-Analyzer-/assets/97799598/565cfdbe-19d7-4760-965a-0e2e4500f7c7) | ![Picture2](https://github.com/astro189/Red-Rover-Analyzer-/assets/97799598/eb836333-5a63-465b-8fd3-bd13c1ded284) 
     
2. **RGB to HSV Conversion:** Converting the RGB image to the HSV color space for improved color representation.
   ![Picture3](https://github.com/astro189/Red-Rover-Analyzer-/assets/97799598/199fa451-4848-4373-8d17-df905b1f29d4)
   
4. **Channel Splitting:** Separating the image into HUE, VALUE, and SATURATION channels to identify the range for masking.
   <span style="display: inline-block; text-align: center;">
       <img src=![Picture4](https://github.com/astro189/Red-Rover-Analyzer-/assets/97799598/70c06397-39e8-4d6c-92f7-d4d81146f0dc) style="width:400px;height:300px;" /> | <img src="images/after_histogram_equalization.png" style="width:400px;height:300px;" />
     </span>
   <span style="display:block;align:center"></span>
   <p align="center">Split channels along with colorbar</p>

6. **Mask Generation:** Creating masks in two steps to isolate the region of interest.
   - *Masked Section 1*
     ![Picture5](https://github.com/astro189/Red-Rover-Analyzer-/assets/97799598/00c9a8fa-f97b-46da-be2d-7aab678793ff)
   - *Masked Section 2*
     ![Picture6](https://github.com/astro189/Red-Rover-Analyzer-/assets/97799598/f18f7c90-9d29-40b4-bc60-b838d8db19fc)
   - *Combined Image*
     ![Picture7](https://github.com/astro189/Red-Rover-Analyzer-/assets/97799598/ac5439ee-f1b9-4eea-82a0-1000a8fefd65)

## Extracting Sand-Filled Region

To extract the sand region, the watershed algorithm is employed. The process involves:

1. **Binarization:** Using OTSU thresholding to create a binary image.

2. **Dilation:** Closing gaps in sand-filled regions.

3. **Distance Transform:** Creating valleys for applying watershed.

4. **Region Extraction:** Comparing pixel intensity from the center to extract the region of interest.

5. **Watershed Segmentation:** Applying watershed to segment the regions.

6. **Final Cropped Image:**
   ![Final Cropped Image](images/final_cropped_image.png)

## Soil Detection Model

The soil detection model is a CNN-based sequential model trained on a small dataset with 5 classes. Details include:

- **Dataset:**
  - Total Images: 156
  - Training Images: 126
  - Validation Images: 30

- **Model Architecture:**
  - Convolutional Layers
  - Pooling Layers (Max Pooling)
  - Fully Connected Layers

- **Hyperparameters:**
  - Batch Size: 10
  - Image Input Size: 220x220
  - Epochs: 30
  - Steps per Epoch: 13
  - Loss Function: Categorical Crossentropy
  - Optimizer: RMSprop

- **Model Training and Validation Performance:**
  - Training Accuracy: 82.23%, Loss: 0.7481
  - Validation Accuracy: 93.33%, Loss: 0.2666

### Model Summary
![Model Summary](images/model_summary.png)

---

## Usage

1. Clone the repository:

```bash
git clone https://github.com/your-username/mars-rover-ai.git
cd mars-rover-ai
