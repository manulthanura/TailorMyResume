import { useState } from 'react';
import ResumeForm from '../components/ResumeForm';

export default function Home() {
  const [feedback, setFeedback] = useState(null);

  const handleSubmit = async (resume, jobDescription) => {
    const formData = new FormData();
    formData.append('resume', resume);
    formData.append('jobDescription', jobDescription);

    const res = await fetch('/api/upload', {
      method: 'POST',
      body: formData,
    });

    const result = await res.json();
    setFeedback(result); // Store feedback in state
  };

  return (
    <div className="container mx-auto p-6">
      <h1 className="text-3xl font-bold mb-6">Resume Feedback App</h1>
      <ResumeForm onSubmit={handleSubmit} />
      {feedback && (
        <div className="mt-6 p-4 bg-gray-100 rounded">
          <h2 className="text-xl font-bold">Resume Feedback</h2>
          <p>Skill Match: {feedback.resume_skill_match}</p>
          <p>Evaluation: {feedback.resume_evaluation}</p>
        </div>
      )}
    </div>
  );
}
