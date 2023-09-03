const ctx2 = document.getElementById("myChart2");

const plugin2 = {
  id: "customCanvasBackgroundColor",
  beforeDraw: (chart, args, options) => {
    const { ctx2 } = chart;
    ctx2.save();
    ctx2.globalCompositeOperation = "destination-over";
    ctx2.fillStyle = options.color || "#fff";
    ctx2.fillRect(0, 0, chart.width, chart.height);
    ctx2.restore();
  },
};

new Chart(ctx2, {
  type: "bar",
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
    backgroundColor: "rgb(255,255,255)",
  },
  plugin2s: [plugin2],
});
