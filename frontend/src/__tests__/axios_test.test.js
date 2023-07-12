import React from 'react';
import { render, screen, fireEvent, waitFor } from '@testing-library/react'
import {BrowserRouter, Router} from 'react-router-dom';
import History from '../pages/History.js';
import VideoDownload from '../pages/VideoDownload.js';
import ImageDownload from '../pages/ImageDownload.js';
import Contact from '../pages/Contact.js';
import mockAxios from "jest-mock-axios";
import FileList from '../components/TextFiles/FileList.js';

test('Test axios POST request for message', () => {
    render(<BrowserRouter><Contact/></BrowserRouter>);
    mockAxios.post= jest.fn().mockResolvedValueOnce('http://127.0.0.1:8000/api/email/',{name: 'John', email: 'mail111@gmail.com', message: 'I found the bug, that this website is too awesome!'});
});

test('Test axios POST request for video upload', () => {
    render(<VideoDownload/>);
    const data = 
        {
            "id": 227,
            "title": "video1",
            "image": "/media/post_videos/mixkit-surprised-man-with-hands-on-head-4508-medium.mp4"
        };
    mockAxios.post(data);
});

test('Test axios POST request for image upload', () => {
    render(<ImageDownload/>);
    const data = 
        {
            "id": 227,
            "title": "image1",
            "image": "/media/post_images/mixkit-surprised-man-with-hands-on-head-4508-medium.png"
        };
    mockAxios.post(data);
});

test('Test axios GET progress', () => {
    render(<VideoDownload/>);
    const data = 
        {
            "task_id": "3ce60697-5bc4-44dd-a5fe-e5755615eaa3", "percent": 100, "state": "SUCCESS", "file": "media\\get_file\\test_video61238252.txt"
        }
    ;
    mockAxios.get(data);
});

test('Test axios GET progress', () => {
    render(<History/>);
    const data = [
        {
            "id": 243,
            "title": "submit",
            "content": "anger : 596, 334, 198, 198 : 0:00:00 : frame 125",
            "file": "http://127.0.0.1:8000/media/get_file/media/get_file/video5610722.txt",
            "created": "2023-06-11T17:39:42.037783Z",
            "data_type": "Video"
        },
        {
            "id": 242,
            "title": "videote",
            "content": "anger : 596, 334, 198, 198 : 0:00:00 : frame 1",
            "file": "http://127.0.0.1:8000/media/get_file/media/get_file/video1611749.txt",
            "created": "2023-06-11T17:36:12.604800Z",
            "data_type": "Video"
        }]
    ;
    mockAxios.get(data);
});

test('FileList component working file download', () => {
    render(<FileList/>);
    FileList.handlePDFDownload=jest.fn();
    FileList.handlePDFDownload(
        {
            "id": 263,
            "title": "image5",
            "content": "sad : 45, 226, 437, 437 ",
            "file": "http://127.0.0.1:8000/media/get_file/media/get_file/sad.txt",
            "created": "2023-06-11T18:38:32.061007Z",
            "data_type": "Image"
        }
    );
});