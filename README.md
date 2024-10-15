# TailorMyResume

TailorMyResume is a powerful tool designed to help job seekers optimize their resumes based on specific job descriptions. Users can upload their job descriptions and resumes in PDF format, and the app provides actionable feedback to enhance alignment with the desired role.

![TailorMyResume Cover Image](./static/images/Repo.png)

## About

A custom pipeline built with Instill Cloud. The application allows users to upload a resume in PDF format and input a job description for detailed analysis. The pipeline extracts text from the PDF, cleans and standardizes it, and matches the resume content with the provided job description. It then generates a skill match report and provides a detailed evaluation, including a suitability score, areas where the candidate meets the job requirements, and suggested improvements.

### Key Features:

- **PDF to Text Conversion**: Utilizes `TASK\_CONVERT\_TO\_TEXT` to extract text content from uploaded resume PDF files.
- **Text Cleaning**: Powered by OpenAI's gpt-4o model for cleaning and standardizing the resume text.
- **Skill Matching**: Compares the cleaned resume against the provided job description, identifying key skills and areas for improvement.
- **Resume Evaluation**: Provides a detailed evaluation report, including a suitability score (0-100) and feedback on strengths and areas for improvement based on the job description.

### Inputs

- **Resume PDF File**: Upload the candidate's resume in PDF format.
- **Job Description**: Paste the job description for comparison and evaluation.

### Outputs:

- **Rate** - Score from 0 to 100 indicating the suitability of the resume for the job description.
- **Skill Matching**: Key skills matched between the resume and job description.
- **Resume Evaluation**: Comprehensive feedback with a suitability score and suggestions for improvement.

## Instill Cloud

[Instill Cloud](https://www.instill.tech/) is a powerful platform that enables the rapid development and deployment of custom AI pipelines. It provides a range of pre-built tasks and models for text analysis, image processing, data extraction, and more. With Instill Cloud, developers can create custom workflows tailored to their specific use cases, allowing for seamless integration of AI capabilities into their applications.

**Project Pipelines**

- [v1beta](./pipelines/v1.2.yaml) - Pipeline that include 4 components and powered by OpenAI's gpt-4o model
- [v2beta](./pipelines/v2.1.yaml) - Comprehensive version of v1beta powered by OpenAI's gpt-4o-mini model

Some resources to get started with Instill Cloud:

- [Explore the Instill Cloud documentation](https://www.instill.tech/docs/welcome)
- [Learn more about OpenAI's models](https://platform.openai.com/docs/models)


### Docker

docker build -t tailormyresume:latest .
docker run --name tailormyresume -p 5000:5000 tailormyresume:latest

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.