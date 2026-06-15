function PredictionCard({ area, current, predicted }) {
    return (
        <div className="card">
            <h3>{area}</h3>
            <p>Current Traffic: {current}</p>
            <p>Predicted Traffic: {predicted}</p>
        </div>
    );
}

export default PredictionCard;