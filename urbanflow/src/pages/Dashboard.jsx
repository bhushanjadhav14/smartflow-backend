import StatCard from "../components/StatCard";

function Dashboard() {
    return (
        <div>
            <h1>Delhi Traffic Dashboard</h1>

            <div className="grid">
                <StatCard title="Traffic Records" value="120K+" />
                <StatCard title="Congested Areas" value="23" />
                <StatCard title="Average Speed" value="42 km/h" />
                <StatCard title="AI Accuracy" value="91%" />
            </div>
        </div>
    );
}

export default Dashboard;