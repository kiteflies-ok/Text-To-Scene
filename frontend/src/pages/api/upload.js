import { CONFIG } from '../../config';

export const config = {
  api: {
    bodyParser: false,
  },
};

export default async function handler(req, res) {
  if (req.method !== 'POST') {
    return res.status(405).json({ error: 'Method not allowed' });
  }

  try {
    const formData = new FormData();
    const file = req.body;
   
    formData.append('file', file);
   
    const backendResponse = await fetch(`${CONFIG.API_BASE_URL}/api/v1/upload-document`, {
      method: 'POST',
      body: formData
    });

    if (!backendResponse.ok) {
      throw new Error('File upload failed');
    }

    const data = await backendResponse.json();
    res.status(200).json(data);
  } catch (error) {
    res.status(500).json({ error: error.message });
  }
}