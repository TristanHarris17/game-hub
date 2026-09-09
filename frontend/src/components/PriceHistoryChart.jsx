import {
    LineChart,
    Line,
    XAxis,
    YAxis,
    CartesianGrid,
    Tooltip,
    ResponsiveContainer,
} from "recharts";

function PriceHistoryChart({ pricehistory }) {
    const chartData = pricehistory
        .filter((price) => price.sale_price != null)
        .map((price) => ({
            date: new Date(price.timestamp).toLocaleDateString(),
            price: price.sale_price,
        }));

    return (
        <ResponsiveContainer width="100%" height={300}>
            <LineChart data={chartData}>
                <CartesianGrid strokeDasharray="3 3" />

                <XAxis dataKey="date" />
                
                <YAxis
                    tickFormatter={(value) => `$${value}`}
                />

                <Tooltip
                    formatter={(value) => [`$${value.toFixed(2)}`, "Price"]}
                />

                <Line
                    type="monotone"
                    dataKey="price"
                    strokeWidth={2}
                />
            </LineChart>
        </ResponsiveContainer>
    )
}

export default PriceHistoryChart;