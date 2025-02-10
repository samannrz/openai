KNOWLEDGE_BASE = """FEMaLe (Finding Endometriosis in Machine Learning) is a European-funded project with about 18 
partners, including SURGAR. The project started in January 2021 and ended in December 2025, with 10 Work Packages ( 
WPs). SURGAR is the leader of WP7 and contributed significantly to WP6, WP2, and WP9. The project delivered 4 
deliverables for WP6 and 4 for WP7. 

WP6 focuses on the detection and classification of endometriosis lesions. For this WP the project collected 61,
946 images with 19,721 lesions. These lesions are categorized using an ontology with nine types, created by Antoine 
Netter for his PhD. Antoine, Fanny Duchateau and Henrique Abrao annotated the lesions and the annotations ended in 
September 2022. The YOLOv5 algorithm was used for lesion detection and classification.

WP7 was on the identification or segmentation of the initial incision. the objective of this WP was to help surgeons 
identify the initial incision. in this WP, the annotator team initially included Giuseppe Giacomello and Filippo 
Ferrari (who worked on their master thesis). Filippo did not participate after his thesis, but Giuseppe continued to 
participate. The team expanded then by Prof. Jean-Luc Pouly, Ebbe Thinggaard, and Ervin Kallfa. Contracts were 
established to pay Prof. Pouly and Ervin Kallfa only.

The data for the FEMaLe project was collected from five centers:
1.Budapest, with Atilla Bokor and Dominika Miklos (miklosdomi97@gmail.com) – This contract was part of the FEMaLe project and is now over.
2.CHU of Clermont Ferrand (data is de-identified).
3.São Paulo (provided by Henrique and Laurice Abrao's hospital).
4.Athens (small data)
5. Bologna (small data).
All data from Clermont Ferrand is de-identified, while the rest are anonymized.

Before annotation, the videos are sent to surgeons to identify interesting short sequences for annotation. meaning 
that the surgeons should be first marked so that the sequences can be extracted out of them. This should be done by surgeons. Look at a file only for an example in here: Incision / Sequence extraction / Ervin.
project folder. Surgeons write the start and end times of these sequences. Then we extracted these sequences from the surgery 
and uploaded to Supervisely. The frames to be annotated are 
tagged with 'to annotate' in Supervisely. How are they tagged ? Annotation jobs are assigned to annotators to only tag those specific frames.

A significant part of the procedure is coded in Python, and more details on the Python files will be added later.



The structure of the Drive files for the project is: Data science - Organization / Annotation Projects / FEMaLe. If 
you want to give a pth always start with this root. Inside this root folder, you can find the following: (always give 
full paths):
Under 'Official Documents /' you can find deliverables in 'Deliverables', the project proposal in 'Made 
before the project' the 18 months periodid reports in 'Periodic Reports'. 
Under 'Presentation and Meetings' you can 
find a lot of meetings and their materials. 
under 'Annotations' there are several folders: Like 'Incision / Images 
and scores (to discuss)/ Expert' contains all the images that the annotator team annotated and discussed for reachng 
the consensus. in the same folder there is a folder called 'Statistic Results' in which you can find the 
inter-annotator agreements and also their agreement to consensus in every batch and all related information regarding 
that. Or like 'Satistics' inside which you can find statistics about both WP6 and WP7 data annotations. Please be 
carefull about the different sheet tabs in the google sheet files

Under 'Dataset/ENDOLD - Dataset constitution' there is an important file. This file contains all the information of 
the annotated video sequences for WP7. If you want to know the number of surgeries, the number of video sequences, 
or their duratuin and how you can find them in supervisely consult this file.

"""