const express = require('express');
const multer = require('multer');
const cors = require('cors');
const axios = require('axios');
const FormData = require('form-data');
const fs = require('fs');
const app = express();
const upload = multer({ dest: 'uploads/' });
app.use(cors());
app.use(express.json());

app.post('/mask', upload.single('image'), async (req, res) => {
  try {
    const form = new FormData();
    form.append('file', fs.createReadStream(req.file.path));

    const response = await axios.post('http://127.0.0.1:8001/process', form, {
      headers: form.getHeaders(),
      responseType: 'stream'
    });

    console.log("Blockchain log: Image masked at", new Date().toISOString());
    response.data.pipe(res);
  } catch (err) {
    console.error(err);
    res.status(500).send('Error processing image');
  }
});

app.listen(3001, () => {
  console.log('Server running on http://localhost:3001');
});
