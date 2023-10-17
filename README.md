# Red-Rover-Analyzer-
## Color-Based Primary Segmentation

The Mars Rover AI employs a color-based segmentation approach to perform primary segmentation of the Martian soil. The following steps outline the process:

1. **Histogram Equalization:** Utilizing CLAHE to enhance image quality by addressing overexposure.
   - *Before Histogram Equalization*
     ![Before Histogram Equalization](images/before_histogram_equalization.png)
   - *After Histogram Equalization*
     ![After Histogram Equalization](images/after_histogram_equalization.png)

2. **RGB to HSV Conversion:** Converting the RGB image to the HSV color space for improved color representation.

3. **Channel Splitting:** Separating the image into HUE, VALUE, and SATURATION channels to identify the range for masking.

4. **Mask Generation:** Creating masks in two steps to isolate the region of interest.
   - *Masked Section 1*
     ![Masked Section 1](images/masked_section_1.png)
   - *Masked Section 2*
     ![Masked Section 2](images/masked_section_2.png)
   - *Combined Image*
     ![Combined Image](images/combined_image.png)

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
