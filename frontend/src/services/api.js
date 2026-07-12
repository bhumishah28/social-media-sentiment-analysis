import axios from "axios";

const API = axios.create({
    baseURL: import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000",
});

export const predictSentiment = async (text) => {

    const response = await API.post(
        "/predict/",
        {
            text,
        }
    );

    return response.data;
};

export const getAnalytics = async () => {

    const response = await API.get(
        "/analytics"
    );

    return response.data;
};

export const getHistory = async () => {

    const response = await API.get(
        "/history"
    );

    return response.data;
};