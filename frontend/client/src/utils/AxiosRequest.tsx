import axios from "axios";

const baseUrl = 'http://127.0.0.1:8000'

const AxiosRequest = axios.create({
    baseURL: baseUrl,
    timeout: 5000,
    headers: {
        Authorization:`Bearer`,
        "Content-Type": "multipart/form-data"
    },
    withCredentials: true
})


export default AxiosRequest