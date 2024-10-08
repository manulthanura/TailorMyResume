import { useState } from 'react';

export default function ResumeForm({ onSubmit }) {
  const [resume, setResume] = useState(null);
  const [jobDescription, setJobDescription] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (resume && jobDescription) {
      onSubmit(resume, jobDescription);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="space-y-4">
      <div>
        <label className="block text-sm font-medium text-gray-700">Upload Resume (PDF)</label>
        <input
          type="file"
          accept="application/pdf"
          onChange={(e) => setResume(e.target.files[0])}
          className="mt-1 block w-full"
        />
      </div>
      <div>
        <label className="block text-sm font-medium text-gray-700">Job Description</label>
        <textarea
          value={jobDescription}
          onChange={(e) => setJobDescription(e.target.value)}
          rows="6"
          className="mt-1 block w-full p-2 border rounded-md"
        />
      </div>
      <button
        type="submit"
        className="bg-blue-500 text-white py-2 px-4 rounded hover:bg-blue-600"
      >
        Submit
      </button>
    </form>
  );
}
