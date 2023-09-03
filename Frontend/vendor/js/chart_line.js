const ctx = document.getElementById("myChart");

const plugin = {
  id: "customCanvasBackgroundColor",
  beforeDraw: (chart, args, options) => {
    const { ctx } = chart;
    ctx.save();
    ctx.globalCompositeOperation = "destination-over";
    ctx.fillStyle = options.color || "#fff";
    ctx.fillRect(0, 0, chart.width, chart.height);
    ctx.restore();
  },
};

new Chart(ctx, {
  type: "line",
  data: {
    labels: ["Red", "Blue", "Yellow", "Green", "Purple", "Orange"],
    datasets: [
      {
        label: "# of Votes",
        data: [12, 19, 3, 5, 2, 3],
        borderWidth: 1,
        backgroundColor: [
          "#007f5f",
          "#55a630",
          "#80b918",
          "#aacc00",
          "#bfd200",
          "#d4d700",
          "#dddf00",
          "#eeef20",
          "#ffff3f",
        ],
        fill: true,
        tension: 0.2,
      },
    ],
  },
  options: {
    scales: {
      y: {
        beginAtZero: true,
        backdropColor: "#111111",
        ticks: {
          color: "black",
        },
      },
      x: {
        grid: {
          tickColor: "black",
        },
        ticks: {
          color: "black",
        },
      },
      tickWidth: 3,
    },
  },
});
