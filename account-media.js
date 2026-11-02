const axios = require('axios');

const options = {
  method: 'GET',
  url: 'https://instagram130.p.rapidapi.com/account-medias',
  params: {
    userid: '7437279263',
    first: '10'
  },
  headers: {
    'X-RapidAPI-Key': process.env.RAPID_API_KEY,
    'X-RapidAPI-Host': 'instagram130.p.rapidapi.com'
  }
};

async function instarequest()
{try {
	const response = await axios.request(options);
	console.log(JSON.stringify(response.data));
} catch (error) {
	console.error(error);
}}

instarequest();