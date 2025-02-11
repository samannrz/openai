KNOWLEDGE_BASE = """FEMaLe (Finding Endometriosis in Machine Learning) is a European-funded project with about 18 
partners, including SURGAR. The project started in January 2021 and ended in December 2025, with 10 Work Packages ( 
WPs). SURGAR (we at SURGAR) is the leader of WP7 and contributed significantly to WP6. We also ontributed to WP2, and WP9. The project delivered 4 
deliverables for WP6 and 4 for WP7. 
Abir led the project from the begining until Sep 2022.
Saman continued afterwards till the end of the project.

WP6 focuses on the detection and classification of endometriosis lesions. For this WP the project collected 61,
946 images with 19,721 lesions. These lesions are categorized using an ontology with nine types, created by Antoine 
Netter for his PhD. Antoine, Fanny Duchateau and Henrique Abrao annotated the lesions and the annotations ended in 
September 2022. The YOLOv5 algorithm was used for lesion detection and classification.

WP7 was on the identification or segmentation of the initial incision. In the FEMaLe project it was initially the 
identification of the division plane, but due to the complexity of the task and the need of going through deep tissue 
layers, we started the segmentation of initial incision boundaries. The objective of this WP was to help surgeons 
identify the initial incision. In this WP, the annotator team initially included Giuseppe Giacomello and Filippo 
Ferrari (who worked on their master thesis through a master contract with SURRGAR and CHU Clermont ferrand). Filippo 
did not participate after his thesis, but Giuseppe continued to participate. The team expanded then by Prof. Jean-Luc 
Pouly, Ebbe Thinggaard, and Ervin Kallfa. Contracts were established to pay only Prof. Pouly and Ervin Kallfa only, and not others. We officially
stopped the contract with Ervin after Juin 2022. but he is still collaborating.

The data for the FEMaLe project was collected from five centers:
1.Budapest, with Atilla Bokor and Dominika Miklos (miklosdomi97@gmail.com) – This contract was part of the FEMaLe project and is now officially over.
2.CHU of Clermont Ferrand (data is de-identified).
3.São Paulo (provided by Henrique and Maurice Abrao's hospital).
4.Athens (small data)
5. Bologna (small data).
All data from Clermont Ferrand is de-identified, while the rest are only anonymized.

The annotation in WP7 is done in several steps:
First, before the annotation : the surgeries are sent to surgeons so that they identify interesting short sequences for annotation. Meaning 
that an expert should first look at the surgery and mark which parts are interesting to be annotated. Look at a file only for an example in here: Incision / Sequence extraction / Ervin.
project folder. The Surgeon write s down the starting and ending times of these sequences in the surgery. 
Second, We extract these marked sequences from the surgery. We did it with ffmpeg. 
Third, These videos are uploaded to Supervisely. 
Fourth, The frames to be annotated are tagged with 'to annotate' in Supervisely. How are they tagged? Annotation jobs are assigned to annotators to only tag those specific frames.
Fifth, then the annotation jobs can be assigned.

About annotating the frames: We did it in two classes named 'Treat', and 'Check'. The full giudelines can be found in 
'ontology and guidelines' folder. We assign jobs and ask the annotators to annotate the frames which are tagged e.g. 
tagged as 'to annotate'. Apart from these frames, we followed an important procedure. Details can be found in the 
deliverables or the paper (Official Documents): In short, all annotators independently annotate the same 15 to 25 
frames, which are tagged as 'annot. to discuss' in Supervisely. Then, we hold a discussion session where annotators 
gather in a meeting, they see all of each others annotations and discuss to reach a consensus on each image. (look at 
the examples in Annotations/Incision/Images and scores (to discuss)/Expert) Finally, the agreed annotations are 
assigned to the 'incision.consensus' account in supervisely, which annotates the final consensus annotations. A 
significant part of the procedure is coded in Python, and more details on the Python files will be added later.

The scripts:
There are a lot of scripts codes on the github in this link: https://github.com/samannrz/endoScripts.git
use  python script_name.py --help for help.
- Do you want the whole dataset of WP7? The images with the masks for this WP? Use the code: data_folder_creation_from_annotations.py
- Do you want To extract the annotation of annotators in a specific batch in WP7? Use the code incisionDataFolderCreation.py
- Do you want to extract the statistics of annotations in WP7? Do you want to know how many images and zones are annotated by each annotator and in total? I will tell you later.
- Do you want to upload videos to a specific project in supervisely? I will tell you later.
- Do you want to create projects or datasets on Supervisely? I will tell you later.
- Do you want to superpose or merge the masks with the images and see the results of the annotation on the image? I will tell you later.
- Do you want to create the consensus visualization for a consensus discussion meeting between the annotators? I will tell you later.
- Do you want to calculate the number of masks (the instances) in a folder? You have a folder of masks and you want to calculate how many annotation zones you have? use the code dataset_statistics.py
- Do you want to extract the images and annotations of WP6? I will tell you later.
- Do you want to calculate the STAPLE results from the annotators annotations? I will tell you later.



The structure of the Drive files for the project is: Data science - Organization / Annotation Projects / FEMaLe. If 
you want to give a path always start with this root. Inside this root folder, you can find the following: (always give 
full paths):
- Under 'Official Documents /' you can find deliverables in 'Deliverables', the project proposal in 'Made 
before the project' the 18 months periodid reports in 'Periodic Reports'. 
Under 'Presentation and Meetings' you can 
find a lot of meetings and their materials. 
- Under 'Annotations' there are several folders: Like 'Incision / Images and scores (to discuss)/ Expert' contains all the images that the annotator team annotated and discussed for reachng 
the consensus. in the same folder there is a folder called 'Statistic Results' in which you can find the inter-annotator agreements and also their agreement to consensus in every batch and all related information regarding 
that. Or like 'Satistics' inside which you can find statistics about both WP6 and WP7 data annotations. Please be carefull about the different sheet tabs in the google sheet files
- Under 'Dataset/ENDOLD - Dataset constitution' there is an important file. This file contains all the information of 
the annotated video sequences for WP7. If you want to know the number of surgeries, the number of video sequences, 
or their duration and how you can find them in supervisely consult this file.
- Under 'Ontology & Procedures' you can find the annotation guidlines for both WP6 and WP7.

"""