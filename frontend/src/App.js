import { BrowserRouter as Router, Routes, Route, } from "react-router-dom";
import Navbar from "./components/Navbar"
import About from "./pages/About"
import History from "./pages/History"
import Contact from "./pages/Contact"
import ImageDownload from "./pages/ImageDownload"
import VideoDownload from "./pages/VideoDownload"
import Home from "./pages"
import Footer from './components/Footer';

// Main App function routing pages
function App() {
  return (
    <div>
      <div classname='navbar'>
        <Router>
          <Navbar/>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/about" element={<About />} />
            <Route path="/history" element={<History />} />
            <Route path="/contact" element={<Contact />} />
            <Route path="/image_upload" element={<ImageDownload />} />
            <Route path="/video_upload" element={<VideoDownload />} />
          </Routes>
        </Router>
      </div>
      <Footer/>
    </div>
  );
}
export default App;