import AlertCard from "../components/AlertCard";

function Alerts() {
    return (
        <div>
            <h1>⚠ Traffic Alerts</h1>

            <AlertCard
                message="Heavy congestion expected near Connaught Place"
            />

            <AlertCard
                message="Traffic spike detected on Ring Road"
            />
        </div>
    );
}

export default Alerts;