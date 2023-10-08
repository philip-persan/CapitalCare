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

const url_rendas = "http://127.0.0.1:8000/rendas/api/v1/rendas/";
const url_investimentos =
  "http://127.0.0.1:8000/investimentos/api/v1/investimentos/";
const url_gastos = "http://127.0.0.1:8000/gastos/api/v1/gastos/";

const fetchOptions = {
  method: "GET",
  credentials: "include",
  headers: {
    "Content-Type": "application/json",
  },
};

function formatToMonthYear(dateString) {
  const [day, month, year] = dateString.split("/");
  const formattedDate = `${year}-${month}-${day}`;

  const date = new Date(formattedDate);
  const monthTwoDigit = (date.getMonth() + 1).toString().padStart(2, "0");
  const yearTwoDigit = date.getFullYear().toString().slice(2);

  return `${monthTwoDigit}/${yearTwoDigit}`;
}

function totalForMonth(dataArray, monthYear) {
  const [month, year] = monthYear.split("/");
  return dataArray
    .filter((item) => formatToMonthYear(item.data) === monthYear)
    .reduce((total, item) => total + item.valor, 0);
}

Promise.all([
  fetch(url_rendas, fetchOptions).then((response) => response.json()),
  fetch(url_investimentos, fetchOptions).then((response) => response.json()),
  fetch(url_gastos, fetchOptions).then((response) => response.json()),
])
  .then(([rendasData, investimentosData, gastosData]) => {
    const allDates = [...rendasData, ...investimentosData, ...gastosData]
      .map((item) => formatToMonthYear(item.data))
      .sort((a, b) => new Date(`01/${a}`) - new Date(`01/${b}`));

    const uniqueDates = [...new Set(allDates)];

    const rendasTotals = uniqueDates.map((monthYear) =>
      totalForMonth(rendasData, monthYear)
    );

    const investimentosTotals = uniqueDates.map((monthYear) =>
      totalForMonth(investimentosData, monthYear)
    );

    const gastosTotals = uniqueDates.map((monthYear) =>
      totalForMonth(gastosData, monthYear)
    );

    new Chart(ctx, {
      type: "line",
      data: {
        labels: uniqueDates,
        datasets: [
          {
            label: "Rendas",
            data: rendasTotals,
            borderColor: "#02C39A", // Primary
            fill: false,
            tension: 0.2,
          },
          {
            label: "Investimentos",
            data: investimentosTotals,
            borderColor: "#7B2CBF", // Accent
            fill: false,
            tension: 0.2,
          },
          {
            label: "Gastos",
            data: gastosTotals,
            borderColor: "#495057", // Neutral Dark Gray
            fill: false,
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
      plugins: [plugin],
    });
  })
  .catch((error) => {
    console.error("Erro ao buscar dados:", error);
  });
