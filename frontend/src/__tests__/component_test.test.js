import React from 'react';
import { render, screen } from '@testing-library/react'
import {BrowserRouter} from 'react-router-dom';
import userEvent from "@testing-library/user-event";
import App from '../App.js'
import Footer from '../components/Footer';
import About from '../pages/About.js';
import History from '../pages/History.js';
import VideoDownload from '../pages/VideoDownload.js';
import ImageDownload from '../pages/ImageDownload.js';
import Contact from '../pages/Contact.js';
import FileList from '../components/TextFiles/FileList.js';
import AnimatedBar from '../components/ProgressBar/ProgressBar.js';
import Tutorial from '../components/Tutorial'

test("Test component footer rendering", () => {
    render(<Footer/>);
    const element = screen.getByText(/© 2023 AER®/i);
    expect(element).toBeInTheDocument();
})

test('Test home page and whether the page renders correctly', () => {
    render(<App/>);
    userEvent.click(screen.getByText(/Home/));
    const element1 = screen.getByText(/Automated tool for recognizing facial emotions in both image and video file./i);
    const element2 = screen.getByText(/Recognition is achieved thanks to implementation of DAN model./i);
    expect(element1).toBeInTheDocument();
    expect(element2).toBeInTheDocument();
    expect(screen.getByRole('link', { name: 'Upload video' })).toHaveAttribute('href', "/video_upload");
    expect(screen.getByRole('link', { name: 'Upload image' })).toHaveAttribute('href', "/image_upload");
});

test('Test history page and whether the page renders correctly', () => {
    render(<History/>);
    expect(screen.getByText(/Show images/i)).toBeInTheDocument();
    expect(screen.getByText(/Show videos/i)).toBeInTheDocument();
    expect(screen.getByText(/Title/i)).toBeInTheDocument();
    expect(screen.getByText(/Created/i)).toBeInTheDocument();
    expect(screen.getByText(/Type/i)).toBeInTheDocument();
});

test('Test about page and whether the page renders correctly', () => {
    render(<About/>);
    expect(screen.getByText(/FAQ - Most frequently asked questions/i)).toBeInTheDocument();
});

test('Test contact page and whether the page renders correctly', () => {
    render(<BrowserRouter><Contact/></BrowserRouter>);
    expect(screen.getByText(/Hi, I'm Paulina Markiewicz! I'm the creator of AER web application/i)).toBeInTheDocument();
    expect(screen.getByRole('link', { class: '{Styles.logo}' })).toHaveAttribute('href', "https://www.linkedin.com/in/paulina-markiewicz-88a708216/");
});


test('Test component progress bar rendering', () => {
    render(<AnimatedBar percent={45}/>);
    expect(screen.getByText(/45/i)).toBeInTheDocument();
});

test('Test component file list rendering', () => {
    render(<FileList/>);
    expect(screen.getByText(/Title/i)).toBeInTheDocument();
    expect(screen.getByText(/Created/i)).toBeInTheDocument();
    expect(screen.getByText(/Type/i)).toBeInTheDocument();
    expect(screen.getByText(/Ops, no files here yet/i)).toBeInTheDocument();
});

test('Test image upload page and whether the page renders correctly', () => {
    render(<ImageDownload/>);
    expect(screen.getByText(/Facial Emotion Recognition for images/i)).toBeInTheDocument();
    expect(screen.getByText(/Submit/i)).toBeInTheDocument();
});

test('Test image upload page download button', () => {
    render(<ImageDownload/>);
    expect(screen.queryByText(/Download/i)).not.toBeInTheDocument();
    expect(screen.queryByText(/Reupload/i)).not.toBeInTheDocument();
});

test('Test video upload page and whether the page renders correctly', () => {
    render(<VideoDownload/>);
    expect(screen.getByText(/Facial Emotion Recognition for videos/i)).toBeInTheDocument();
    expect(screen.getByText(/Submit/i)).toBeInTheDocument();
});

test('Test video page function handleStart', () => {
    render(<VideoDownload/>);
    const before_finished=VideoDownload.finito;
    VideoDownload.handleStart=jest.fn();
    VideoDownload.handleStart();
    expect(before_finished).toEqual(VideoDownload.finito);
});

test('Test video page function handleImageChange', () => {
    render(<VideoDownload/>);
    const before_finished=VideoDownload.state;
    VideoDownload.handleImageChange=jest.fn();
    VideoDownload.handleImageChange();
    expect(before_finished).toEqual(VideoDownload.state);
});

test('Test video page function handleChange', () => {
    render(<VideoDownload/>);
    const before_finished=VideoDownload.state;
    VideoDownload.handleChange=jest.fn();
    VideoDownload.handleChange();
    expect(before_finished).toEqual(VideoDownload.state);
});

test("Test component tutorial rendering", () => {
    render(<Tutorial/>);
    const element1 = screen.getByText(/I. Image mode/i);
    expect(element1).toBeInTheDocument();
    const element2 = screen.getByText(/II. Video mode/i);
    expect(element2).toBeInTheDocument();
})