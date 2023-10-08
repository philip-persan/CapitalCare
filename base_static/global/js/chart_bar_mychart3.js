const ctx3 = document.getElementById("myChart3");

const plugin3 = {
  id: "customCanvasBackgroundColor",
  beforeDraw: (chart, args, options) => {
    const { ctx3 } = chart;
    ctx3.save();
    ctx3.globalCompositeOperation = "destination-over";
    ctx3.fillStyle = options.color || "#fff";
    ctx3.fillRect(0, 0, chart.width, chart.height);
    ctx3.restore();
  },
};

const url3 = "http://127.0.0.1:8000/gastos/api/v1/annotations/";

fetch(url3, {
  method: "GET",
  credentials: "include",
  headers: {
    "Content-Type": "application/json",
  },
})
  .then((response) => response.json())
  .then((data) => {
    const totalsByCategory = data.por_categoria;
    const labels = totalsByCategory.map(
      (item) => item.categoria__nome_categoria
    );
    const values = totalsByCategory.map((item) =>
      parseFloat(item.total_por_categoria)
    );

    new Chart(ctx3, {
      type: "bar",
      data: {
        labels: labels,
        datasets: [
          {
            label: "Valor R$",
            data: values,
            borderWidth: 1,
            backgroundColor: [
              "#02C39A", // Primary
              "#7B2CBF", // Accent
              "#495057", // Neutral Dark Gray
              "#DEE2E6", // Neutral Light Gray
              "#D8D9FA", // Neutral Light
            ],
          },
        ],
      },
      options: {
        plugins: {
          title: {
            display: true,
            text: "Gastos por Categoria",
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
        backgroundColor: "rgba(0, 0, 0, 0)",
      },
      plugin3s: [plugin3],
    });
  });
