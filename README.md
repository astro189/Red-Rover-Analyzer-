# Red-Rover-Analyzer-
### Problem Stament: 
Develop a robotic arm capable of autonomously analyzing soil samples and reporting various properties
<h4>List of features required:</h4>
<li> Identify sand-filled against empty regions in the box</li>
<li> Take sample from the section of the box with the soil </li>
<li> Report back the soil type</li>

## Color-Based Primary Segmentation

The Mars Rover AI employs a color-based segmentation approach to perform primary segmentation of the Martian soil. The following steps outline the process:

1. **Histogram Equalization:** Utilizing CLAHE to enhance image quality by addressing foggy sections of the image.

   <div align="center" style="display: flex; justify-content: space-between;">
        <table>
           <tr>
             <td align="center">
               <img src="https://github.com/astro189/Red-Rover-Analyzer-/blob/main/Images/Picture1.jpg" alt="Section 1" width="300">
               <p><b>Before Histogram Equalization</b></p>
             </td>
             <td align="center">
               <img src="https://github.com/astro189/Red-Rover-Analyzer-/blob/main/Images/Picture2.jpg" alt="Section 2" width="300">
               <p><b>After Histogram Equalization</b></p>
             </td>
           </tr>
      </table>
  </div>

     
2. **RGB to HSV Conversion:** Converting the RGB image to the HSV color space for improved color representation.
   <p align="center">
     <img src="https://github.com/astro189/Red-Rover-Analyzer-/blob/main/Images/Picture3.jpg" alt="HSV Image" width="300"/>
   </p>
   <p align="center" ><b>Image in HSV space</b></p>
4. **Channel Splitting:** Separating the image into HUE, VALUE, and SATURATION channels to identify the range for masking.
   <p align="center">
     <img src="https://github.com/astro189/Red-Rover-Analyzer-/blob/main/Images/Picture4.jpg" alt="Split channel" width="600"/>
   </p>
   <p align="center"><b>Split channels along with colorbar</b></p>

6. **Mask Generation:** Creating masks in two steps to isolate the region of interest.
  <div align="center" style="display: flex; justify-content: space-between;">
        <table>
           <tr>
             <td align="center">
               <img src="https://github.com/astro189/Red-Rover-Analyzer-/blob/main/Images/Picture5.jpg" alt="Section 1" width="300">
               <p><b>Section 1</b></p>
             </td>
             <td align="center">
               <img src="https://github.com/astro189/Red-Rover-Analyzer-/blob/main/Images/Picture6.jpg" alt="Section 2" width="300">
               <p><b>Section 2</b></p>
             </td>
           </tr>
      </table>
  </div>
  <div align="center" style="display: flex; justify-content: space-between;">
     <img src="https://github.com/astro189/Red-Rover-Analyzer-/blob/main/Images/Picture7.jpg" alt="Section 2" width="300">
     <p><b>Combined Image</b></p>
  </div>

## Extracting Sand-Filled Region

To extract the sand region, the watershed algorithm is employed. The process involves:

1. **Binarization:** Using OTSU thresholding to create a binary image.

2. **Dilation:** Closing gaps in sand-filled regions.

3. **Distance Transform:** Creating valleys for applying watershed.

4. **Region Extraction:** Comparing pixel intensity from the center to extract the region of interest.

5. **Watershed Segmentation:** Applying watershed to segment the regions.

6. **Final Cropped Image:** Cropping the unnecessary background

<img src="https://github.com/astro189/Red-Rover-Analyzer-/blob/main/Images/Screenshot%202023-10-19%20000752.png" alt="Flow chart"></img>

## Soil Detection Model

The soil detection model is a CNN-based sequential model trained on a dataset with 5 classes corresponding to the types of mentioned in the problem statement . Details include:

- **Model Architecture:**
  <p align="center">
  <img src="https://github.com/astro189/Red-Rover-Analyzer-/blob/main/Images/Model.jpg" alt="Model Architecture" width="600"></img>
  </p>

- **Hyperparameters:**
  - Batch Size: 10
  - Image Input Size: 220x220
  - Epochs: 30
  - Steps per Epoch: 13
  - Loss Function: Categorical Crossentropy
  - Optimizer: RMSprop

- **Model Training and Validation Performance:**
  - Training Accuracy: 91.23%, Loss: 0.3781
  - Validation Accuracy: 93.33%, Loss: 0.2666
</br>
  <div align="center" style="display: flex; justify-content: space-between;">
        <table>
           <tr>
             <td align="center">
               <img src="https://github.com/astro189/Red-Rover-Analyzer-/blob/main/Images/Picture16.jpg" alt="Accuracy Plot" width="300">
             </td>
             <td align="center">
               <img src="https://github.com/astro189/Red-Rover-Analyzer-/blob/main/Images/Picture17.jpg" alt="Loss Plot" width="300">
             </td>
           </tr>
      </table>
  </div>

## Usage

1. Clone the repository:

```bash
git clone https://github.com/astro189/Red-Rover-Analyzer-.git
cd Red-Rover-Analyzer
