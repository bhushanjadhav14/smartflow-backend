function AlertCard({ message }) {
    return (
        <div className="card">
            <p>⚠ {message}</p>
        </div>
    );
}

export default AlertCard;