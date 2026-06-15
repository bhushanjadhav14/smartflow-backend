function RouteForm() {
    return (
        <div>
            <input
                type="text"
                placeholder="Source"
                style={{ margin: "10px" }}
            />

            <input
                type="text"
                placeholder="Destination"
                style={{ margin: "10px" }}
            />

            <button>Find Route</button>
        </div>
    );
}

export default RouteForm;