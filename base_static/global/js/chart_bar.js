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

const url = "http://127.0.0.1:8000/rendas/api/v1/rendas/";

fetch(url, {
  method: "GET",
  credentials: "include", // Essencial para enviar cookies com a requisição
  headers: {
    "Content-Type": "application/json",
  },
})
  .then((response) => response.json())
  .then((data) => {
    const totalsByType = data.reduce((acc, item) => {
      if (!acc[item.tipo]) {
        acc[item.tipo] = 0;
      }
      acc[item.tipo] += item.valor;
      return acc;
    }, {});
    const labels = Object.keys(totalsByType);
    const values = labels.map((label) =>
      parseFloat(totalsByType[label].toFixed(2))
    );

    new Chart(ctx2, {
      type: "bar",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Valor R$",
            data: values,
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
        plugins: {
          title: {
            display: true,
            text: "Valor por Renda",
          },
        },
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
  });
