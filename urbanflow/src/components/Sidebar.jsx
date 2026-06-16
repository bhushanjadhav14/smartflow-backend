import { Link } from "react-router-dom";

function Sidebar() {
    return (
        <div className="sidebar">
            <h2>🚦 UrbanFlow</h2>

            <Link to="/">Dashboard</Link>
            <Link to="/traffic">Live Traffic</Link>
            <Link to="/predictions">Predictions</Link>
            <Link to="/alerts">Alerts</Link>
            <Link to="/route">Route Planner</Link>
            <Link to="/about">About</Link>
        </div>
    );
}

export default Sidebar;