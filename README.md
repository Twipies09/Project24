# Project24

Oakridge Codefest '24

Team: Veekshith, Pranav, Jimit, Tanisha, Sanjana

# Active Groups
ppt group    : Sanjana,
               Tanisha.

# Logs
- Topic and idea finalised (1/1) {10-1-24} 
- v0.0.1 (1/2) {10-1-24}
    - Presentation [Ppt group] (0/1)
    - Application [Ui group, Dataset group, Ai group] (3/3)

# Notes

		INTRO

1. famous ppl who died of cancer
2. cancer statistic (evergrowing, highest predicted cause of death)
3. why? (late detection, bad doctors)
	even though we hav working treatment options such as radiotherapy, surgery or immunotherapy, late detection and bad doctors lead to the reoccuronce and death due to this disease
4. intro of our solution
	CDSN - Cancer Detection and Segmentation Net
	cancer detection from ct scans and radiotherapy where it will detect all cancer tumors including MCTs and 4 mm overlay instead of 6mm which will save millions of healthy cells.

		MAIN
1. datsets (dicom 3d - conv to multiple jpg at angle and diff exposures)
2. semantic class segemntation
3. SOTA object detection using each decomposed relay from u net arch
4. our architecture (2., 3.) U-Arch cnn architecture
5. self annotation and augmentation
	Till now models were only as good as the doctors who annotated the datasets the model ws trained upon, but why does it have to be that way? after all a doctor cant understand 
	a image as well as our segemntation model.

	So we used self annotation and augmentation tools so the model learns how to find cancer strains even the best doctors cant find. so now our model can even detect  microscopic
	cancer tumors and reduce the reoccurance rate of cancer
6. model stats (accuracy, false-positive rate, time)
7. edge compution capabilities
	this model will run on _____ (my comp specs(v bad)) in our demo
	so it can easily run on say a jetson which will be integrated to ct-scan and radiotherapy equipment.

		FUTURE PLANS
8. use model for colorectal and pancreatic cancer (close relatives of lung cancer.)
	explain why this model will be vry helpful in the detection and treatment of these cancers (rishabh jain)
9. develop another submodel (with similar architecture) to work with endoscopic cameras (help during surgery)
10. research more on the viability of self annotation and augmentation in cancer. 
    get medical lisence so this can be implemented in hospitals. 

		ABOUT US
11. tell them another teammate will give a brief introduction about us while we get the demo ready
12. about us (achievements and qualifications)
13. DEMO (1 ct scan that the model has never seen b4)

14. QnA session.
