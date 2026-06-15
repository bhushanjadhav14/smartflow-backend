import PredictionCard from "../components/PredictionCard";

function Predictions() {
    return (
        <div>
            <h1>🤖 AI Predictions</h1>

            <div
                style={{
                    display: "grid",
                    gridTemplateColumns: "repeat(3,1fr)",
                    gap: "20px",
                }}
            >
                <PredictionCard
                    area="Connaught Place"
                    current="65%"
                    predicted="82%"
                />

                <PredictionCard
                    area="Karol Bagh"
                    current="55%"
                    predicted="75%"
                />

                <PredictionCard
                    area="Rohini"
                    current="42%"
                    predicted="60%"
                />
            </div>
        </div>
    );
}

export default Predictions;