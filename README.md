# resume-screener
**Objective**
- Given the job description screen the candidate resume based on customized evaluation criteria for skills, experience, qualifications, and personality traits  set by employer  

### Set up
- Use vertex workbench with python 3.10
- Clone this repository in Vertex workbench
- Install dependencies present in requirements.txt
  
### Datasets
1. <a href="https://www.kaggle.com/datasets/saugataroyarghya/resume-dataset">Kaggle dataset</a> for candidate resume
2. <a href="https://business.linkedin.com/talent-solutions/resources/how-to-hire-guides/software-engineer/job-description">Linkedin template</a> resume for job descrition (Extracted text is present inside experiments/data folder)

### Notebooks (Execute them in sequence)
- **[experiments/target-cv-analyzer.ipynb](resume-screener/experiments/target-cv-analyzer.ipynb):** Parse linkedin job resume and get fields in structured format
-  **[experiments/parse-candidate_resumes.ipynb](resume-screener/experiments/parse-candidate_resumes.ipynb):** Parse candidate resumes and get fields in structured format
-  **[experiments/model.py](resume-screener/experiments/model.py):** Model definition for structured format
-  **[experiments/candidate_evaluation.ipynb](resume-screener/experiments/candidate_evaluation.ipynb):** Contains the logic for ranking and evaluating the candidates based on customized criteria and select top 3 candidates

