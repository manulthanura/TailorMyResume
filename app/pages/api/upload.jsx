export const config = {
    api: {
      bodyParser: false, // Disable body parsing for file uploads
    },
  };
  
  import formidable from 'formidable';
  import fs from 'fs';
  
  const parseForm = (req) => {
    return new Promise((resolve, reject) => {
      const form = new formidable.IncomingForm();
      form.parse(req, (err, fields, files) => {
        if (err) reject(err);
        resolve({ fields, files });
      });
    });
  };
  
  const uploadHandler = async (req, res) => {
    if (req.method === 'POST') {
      const { fields, files } = await parseForm(req);
  
      const resumePath = files.resume.filepath;
      const jobDescription = fields.jobDescription;
  
      // Here, you would handle the Instill Cloud API request
      const instillApiResponse = await fetch('https://api.instill.tech/v1/pipelines', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          Authorization: 'Bearer YOUR_API_KEY', // Replace with your Instill Cloud API key
        },
        body: JSON.stringify({
          resume_pdf_file: fs.readFileSync(resumePath),
          job_description: jobDescription,
        }),
      });
  
      const feedback = await instillApiResponse.json();
  
      res.status(200).json(feedback); // Send the response back to the client
    } else {
      res.status(405).send('Method Not Allowed');
    }
  };
  
  export default uploadHandler;
  