import { Routes, Route } from "react-router-dom";

import Sidebar from "./components/Sidebar";

import Dashboard from "./pages/Dashboard";
import LiveTraffic from "./pages/LiveTraffic";
import Predictions from "./pages/Predictions";
import Alerts from "./pages/Alerts";
import RoutePlanner from "./pages/RoutePlanner";
import About from "./pages/About";

function App() {
  return (
    <div className="app">
      <Sidebar />

      <div className="content">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/traffic" element={<LiveTraffic />} />
          <Route path="/predictions" element={<Predictions />} />
          <Route path="/alerts" element={<Alerts />} />
          <Route path="/route" element={<RoutePlanner />} />
          <Route path="/about" element={<About />} />
        </Routes>
      </div>
    </div>
  );
}

export default App;