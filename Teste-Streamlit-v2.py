{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "nOIid0WMCNB2"
   },
   "source": [
    "# **Definição das Bibliotecas**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting psycopg2\n",
      "  Downloading psycopg2-2.9.9-cp312-cp312-win_amd64.whl.metadata (4.5 kB)\n",
      "Downloading psycopg2-2.9.9-cp312-cp312-win_amd64.whl (1.2 MB)\n",
      "   ---------------------------------------- 0.0/1.2 MB ? eta -:--:--\n",
      "   ---------------------------------------- 0.0/1.2 MB ? eta -:--:--\n",
      "   --- ------------------------------------ 0.1/1.2 MB 1.3 MB/s eta 0:00:01\n",
      "   -------- ------------------------------- 0.3/1.2 MB 2.2 MB/s eta 0:00:01\n",
      "   -------------- ------------------------- 0.4/1.2 MB 2.9 MB/s eta 0:00:01\n",
      "   --------------------- ------------------ 0.6/1.2 MB 3.2 MB/s eta 0:00:01\n",
      "   --------------------------- ------------ 0.8/1.2 MB 3.4 MB/s eta 0:00:01\n",
      "   ------------------------------------ --- 1.1/1.2 MB 3.8 MB/s eta 0:00:01\n",
      "   ---------------------------------------- 1.2/1.2 MB 3.9 MB/s eta 0:00:00\n",
      "Installing collected packages: psycopg2\n",
      "Successfully installed psycopg2-2.9.9\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install psycopg2 "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {
    "id": "IToXB5c9Q1iq"
   },
   "outputs": [],
   "source": [
    "import psycopg2\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "import plotly.express as px"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "jYqQwQNxCVl6"
   },
   "source": [
    "# **Conexão com o Banco de Dados DATA_IESB**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "gmX8q1C5RAWo",
    "outputId": "e9d06d25-8952-4401-a8a1-b43729c9e342"
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Conexão bem-sucedida!\n"
     ]
    }
   ],
   "source": [
    "try:\n",
    "    conn = psycopg2.connect(\n",
    "      dbname=\"Data_IESB\",\n",
    "      user=\"Data_IESB\",\n",
    "      password=\"DATA_IESB\",\n",
    "      host=\"dataiesb.iesbtech.com.br\",\n",
    "      port=\"5432\"\n",
    "    )\n",
    "    print(\"Conexão bem-sucedida!\")\n",
    "except psycopg2.Error as e:\n",
    "    print(\"Erro ao conectar ao PostgreSQL:\", e)\n",
    "\n",
    "cur = conn.cursor()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "lXkUq8mLChSZ"
   },
   "source": [
    "# **Leitura de uma view do Banco de Dados**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/"
    },
    "id": "DZOn_3Vikmm9",
    "outputId": "4bff5686-0345-4437-c7e9-d5afbeab9f14"
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\sergi\\AppData\\Local\\Temp\\ipykernel_57192\\3364509361.py:1: UserWarning: pandas only supports SQLAlchemy connectable (engine/connection) or database string URI or sqlite3 DBAPI2 connection. Other DBAPI2 objects are not tested. Please consider using SQLAlchemy.\n",
      "  view_populacao = pd.read_sql_query(\"SELECT * FROM Brasil_Populacao\", conn)\n"
     ]
    }
   ],
   "source": [
    "view_populacao = pd.read_sql_query(\"SELECT * FROM Brasil_Populacao\", conn)\n",
    "\n",
    "conn.close()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {
    "id": "mAs7XUSLC2xL"
   },
   "source": [
    "# **Exemplo de criação de um gráfico usando uma visão do banco de dados**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {
    "colab": {
     "base_uri": "https://localhost:8080/",
     "height": 542
    },
    "id": "rCbl38wtB8Uq",
    "outputId": "3bf85328-4527-402d-8594-6108c98e4d93"
   },
   "outputs": [
    {
     "data": {
      "application/vnd.plotly.v1+json": {
       "config": {
        "plotlyServerURL": "https://plot.ly"
       },
       "data": [
        {
         "alignmentgroup": "True",
         "hovertemplate": "Nome da Região=%{x}<br>Número de Habitantes=%{y}<extra></extra>",
         "legendgroup": "",
         "marker": {
          "color": "#636efa",
          "pattern": {
           "shape": ""
          }
         },
         "name": "",
         "offsetgroup": "",
         "orientation": "v",
         "showlegend": "false",
         "textposition": "auto",
         "type": "bar",
         "x": [
          "Centro-Oeste",
          "Nordeste",
          "Norte",
          "Sudeste",
          "Sul"
         ],
         "xaxis": "x",
         "y": [
          16289538,
          54658515,
          17354884,
          84840113,
          29937706
         ],
         "yaxis": "y"
        }
       ],
       "layout": {
        "autosize": "true",
        "barmode": "relative",
        "legend": {
         "tracegroupgap": 0
        },
        "template": {
         "data": {
          "bar": [
           {
            "error_x": {
             "color": "#2a3f5f"
            },
            "error_y": {
             "color": "#2a3f5f"
            },
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "bar"
           }
          ],
          "barpolar": [
           {
            "marker": {
             "line": {
              "color": "#E5ECF6",
              "width": 0.5
             },
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "barpolar"
           }
          ],
          "carpet": [
           {
            "aaxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "baxis": {
             "endlinecolor": "#2a3f5f",
             "gridcolor": "white",
             "linecolor": "white",
             "minorgridcolor": "white",
             "startlinecolor": "#2a3f5f"
            },
            "type": "carpet"
           }
          ],
          "choropleth": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "choropleth"
           }
          ],
          "contour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "contour"
           }
          ],
          "contourcarpet": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "contourcarpet"
           }
          ],
          "heatmap": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmap"
           }
          ],
          "heatmapgl": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "heatmapgl"
           }
          ],
          "histogram": [
           {
            "marker": {
             "pattern": {
              "fillmode": "overlay",
              "size": 10,
              "solidity": 0.2
             }
            },
            "type": "histogram"
           }
          ],
          "histogram2d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2d"
           }
          ],
          "histogram2dcontour": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "histogram2dcontour"
           }
          ],
          "mesh3d": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "type": "mesh3d"
           }
          ],
          "parcoords": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "parcoords"
           }
          ],
          "pie": [
           {
            "automargin": true,
            "type": "pie"
           }
          ],
          "scatter": [
           {
            "fillpattern": {
             "fillmode": "overlay",
             "size": 10,
             "solidity": 0.2
            },
            "type": "scatter"
           }
          ],
          "scatter3d": [
           {
            "line": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatter3d"
           }
          ],
          "scattercarpet": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattercarpet"
           }
          ],
          "scattergeo": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergeo"
           }
          ],
          "scattergl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattergl"
           }
          ],
          "scattermapbox": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scattermapbox"
           }
          ],
          "scatterpolar": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolar"
           }
          ],
          "scatterpolargl": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterpolargl"
           }
          ],
          "scatterternary": [
           {
            "marker": {
             "colorbar": {
              "outlinewidth": 0,
              "ticks": ""
             }
            },
            "type": "scatterternary"
           }
          ],
          "surface": [
           {
            "colorbar": {
             "outlinewidth": 0,
             "ticks": ""
            },
            "colorscale": [
             [
              0,
              "#0d0887"
             ],
             [
              0.1111111111111111,
              "#46039f"
             ],
             [
              0.2222222222222222,
              "#7201a8"
             ],
             [
              0.3333333333333333,
              "#9c179e"
             ],
             [
              0.4444444444444444,
              "#bd3786"
             ],
             [
              0.5555555555555556,
              "#d8576b"
             ],
             [
              0.6666666666666666,
              "#ed7953"
             ],
             [
              0.7777777777777778,
              "#fb9f3a"
             ],
             [
              0.8888888888888888,
              "#fdca26"
             ],
             [
              1,
              "#f0f921"
             ]
            ],
            "type": "surface"
           }
          ],
          "table": [
           {
            "cells": {
             "fill": {
              "color": "#EBF0F8"
             },
             "line": {
              "color": "white"
             }
            },
            "header": {
             "fill": {
              "color": "#C8D4E3"
             },
             "line": {
              "color": "white"
             }
            },
            "type": "table"
           }
          ]
         },
         "layout": {
          "annotationdefaults": {
           "arrowcolor": "#2a3f5f",
           "arrowhead": 0,
           "arrowwidth": 1
          },
          "autotypenumbers": "strict",
          "coloraxis": {
           "colorbar": {
            "outlinewidth": 0,
            "ticks": ""
           }
          },
          "colorscale": {
           "diverging": [
            [
             0,
             "#8e0152"
            ],
            [
             0.1,
             "#c51b7d"
            ],
            [
             0.2,
             "#de77ae"
            ],
            [
             0.3,
             "#f1b6da"
            ],
            [
             0.4,
             "#fde0ef"
            ],
            [
             0.5,
             "#f7f7f7"
            ],
            [
             0.6,
             "#e6f5d0"
            ],
            [
             0.7,
             "#b8e186"
            ],
            [
             0.8,
             "#7fbc41"
            ],
            [
             0.9,
             "#4d9221"
            ],
            [
             1,
             "#276419"
            ]
           ],
           "sequential": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ],
           "sequentialminus": [
            [
             0,
             "#0d0887"
            ],
            [
             0.1111111111111111,
             "#46039f"
            ],
            [
             0.2222222222222222,
             "#7201a8"
            ],
            [
             0.3333333333333333,
             "#9c179e"
            ],
            [
             0.4444444444444444,
             "#bd3786"
            ],
            [
             0.5555555555555556,
             "#d8576b"
            ],
            [
             0.6666666666666666,
             "#ed7953"
            ],
            [
             0.7777777777777778,
             "#fb9f3a"
            ],
            [
             0.8888888888888888,
             "#fdca26"
            ],
            [
             1,
             "#f0f921"
            ]
           ]
          },
          "colorway": [
           "#636efa",
           "#EF553B",
           "#00cc96",
           "#ab63fa",
           "#FFA15A",
           "#19d3f3",
           "#FF6692",
           "#B6E880",
           "#FF97FF",
           "#FECB52"
          ],
          "font": {
           "color": "#2a3f5f"
          },
          "geo": {
           "bgcolor": "white",
           "lakecolor": "white",
           "landcolor": "#E5ECF6",
           "showlakes": true,
           "showland": true,
           "subunitcolor": "white"
          },
          "hoverlabel": {
           "align": "left"
          },
          "hovermode": "closest",
          "mapbox": {
           "style": "light"
          },
          "paper_bgcolor": "white",
          "plot_bgcolor": "#E5ECF6",
          "polar": {
           "angularaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "radialaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "scene": {
           "xaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "yaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           },
           "zaxis": {
            "backgroundcolor": "#E5ECF6",
            "gridcolor": "white",
            "gridwidth": 2,
            "linecolor": "white",
            "showbackground": true,
            "ticks": "",
            "zerolinecolor": "white"
           }
          },
          "shapedefaults": {
           "line": {
            "color": "#2a3f5f"
           }
          },
          "ternary": {
           "aaxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "baxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           },
           "bgcolor": "#E5ECF6",
           "caxis": {
            "gridcolor": "white",
            "linecolor": "white",
            "ticks": ""
           }
          },
          "title": {
           "x": 0.05
          },
          "xaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          },
          "yaxis": {
           "automargin": true,
           "gridcolor": "white",
           "linecolor": "white",
           "ticks": "",
           "title": {
            "standoff": 15
           },
           "zerolinecolor": "white",
           "zerolinewidth": 2
          }
         }
        },
        "title": {
         "text": "População por Região"
        },
        "xaxis": {
         "anchor": "y",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          -0.5,
          4.5
         ],
         "title": {
          "text": "Nome da Região"
         },
         "type": "category"
        },
        "yaxis": {
         "anchor": "x",
         "autorange": true,
         "domain": [
          0,
          1
         ],
         "range": [
          0,
          89305382.10526316
         ],
         "title": {
          "text": "Número de Habitantes"
         },
         "type": "linear"
        }
       }
      },
      "image/png": "iVBORw0KGgoAAAANSUhEUgAABE0AAAFoCAYAAACixgUDAAAAAXNSR0IArs4c6QAAIABJREFUeF7t3X+wH2WdL/gnASFYxAh4CcTLBYGpDTgoIxfN3V25ueKUGi41s7lrBsUZMVYmC7fGEqhQCRbFpSxJKqkAq1VksikDXmUMYZdxiiFq7eAwOFOTkcFhLi6wNYAiY/ixIoPogAjJ1vN1+tw+ne85p7/pb/f36e7X+UPhpLufz/P69Dmc887TT887cODAgeCDAAECBAgQIECAAAECBAgQIEBgmsA8oYk7ggABAgQIECBAgAABAgQIECBwsIDQxF1BgAABAgQIECBAgAABAgQIEBgiIDRxWxAgQIAAAQIECBAgQIAAAQIEhCbuAQIECBAgQIAAAQIECBAgQIBAOQErTco5OYoAAQIECBAgQIAAAQIECBDomYDQpGcNN10CBAgQIECAAAECBAgQIECgnIDQpJyTowgQIECAAAECBAgQIECAAIGeCQhNetZw0yVAgAABAgQIECBAgAABAgTKCQhNyjk5igABAgQIECBAgAABAgQIEOiZgNCkZw03XQIECBAgQIAAAQIECBAgQKCcgNCknJOjCBAgQIAAAQIECBAgQIAAgZ4JCE161nDTJUCAAAECBAgQIECAAAECBMoJCE3KOTmKAAECBAgQIECAAAECBAgQ6JmA0KRnDTddAgQIECBAgAABAgQIECBAoJyA0KSck6MIECBAgAABAgQIECBAgACBngkITXrWcNMlQIAAAQIECBAgQIAAAQIEygkITco5OYoAAQIECBAgQIAAAQIECBDomYDQpGcNN10CBAgQIECAAAECBAgQIECgnIDQpJyTowgQIECAAAECBAgQIECAAIGeCQhNetZw0yVAgAABAgQIECBAgAABAgTKCQhNyjk5igABAgQIECBAgAABAgQIEOiZgNCkZw03XQIECBAgQIAAAQIECBAgQKCcgNCknJOjCBAgQIAAAQIECBAgQIAAgZ4JCE161nDTJUCAAAECBAgQIECAAAECBMoJCE3KOTmKAAECBAgQIECAAAECBAgQ6JmA0KRnDTddAgQIECBAgAABAgQIECBAoJyA0KSck6MIECBAgAABAgQIECBAgACBngkITXrWcNMlQIAAAQIECBAgQIAAAQIEygkITco5OYoAAQIECBAgQIAAAQIECBDo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TWJwET/ia3Kb/uh6aBLn9973vCOce/bSKdqyG8k23QvjESBAgAABAgQIECBAgEA1AaHJiH6phib5x1xGeZxmxOnPeXgfQpMvfnXPNIdsb5Q5cRxAgAABAgQIECBAgAABAq0SEJq0ql2KJUCAAAECBAgQIECAAAECBJoSEJo0JW0cAgQIECBAgAABAgQIECBAoFUCQpNWtUuxBAgQIECAAAECBAgQIECAQFMCQpOmpI1DgAABAgQIECBAgAABAgQItEpAaNKqdimWAAECBAgQIECAAAECBAgQaEpAaNKUtHEIECBAgAABAgQIECBAgACBVgkITVrVLsUSIECAAAECBAgQIECAAAECTQkITZqSNg4BAgQIECBAgAABAgQIECDQKgGhSavapVgCBAgQIECAAAECBAgQIECgKQGhSVPSxiFAgAABAgQIECBAgAABAgRaJSA0aVW7FEuAAAECBAgQIECAAAECBAg0JSA0aUraOAQIECBAgAABAgQIECBAgECrBIQmrWqXYgkQIECAAAECBAgQIECAAIGmBIQmTUkbhwABAgQIECBAgAABAgQIEGiVgNCkVe1SLAECBAgQIECAAAECBAgQINCUgNCkKWnjECBAgAABAgQIECBAgAABAq0SEJq0ql2KJUCAAAECBAgQIECAAAECBJoSEJo0JW0cAgQIECBAgAABAgQIECBAoFUCQpNWtUuxBAgQIECAAAECBAgQIECAQFMCQpOmpI1DgAABAgQIECBAgAABAgQItEpAaNKqdimWAAECBAgQIECAAAECBAgQaEpAaNKUtHEIECBAgAABAgQIECBAgACBVgkITVrVLsUSIECAAAECBAgQIECAAAECTQkITZqSNg4BAgQIECBAgAABAgQIECDQKgGhSavapVgCBAgQIECAAAECBAgQIECgKQGhSVPSxiFAgAABAgQIECBAgAABAgRaJSA0aVW7FEuAAAECBAgQIECAAAECBAg0JSA0aUraOAQIECBAgAABAgQIECBAgECrBIQmrWqXYgkQIECAAAECBAgQIECAAIGmBIQmTUkbhwABAgQIECBAgAABAgQIEGiVgNCkVe1SLAECBAgQIECAAAECBAgQINCUgNCkKWnjECBAgAABAgQIECBAgAABAq0SEJq0ql2KJUCAAAECBAgQIECAAAECBJoSEJo0JW0cAgQIECBAgAAB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Ya7WxHDhjrvunbbHSDE0ifO4ZvPOkO1xks2tuDdJfqziYzZZ6LLife+ZCkCGrZ4p1jvXSpS4KqS4ciSes+dbfzP1GFOxN3P5C03mumv8OQECBAgQSENAaJJGH1RBgAABAgRKCRRDkywUOProN4aH/9/vT4Umcz0eUuXxnNmCjGGTKLPSZFjIMGwOs4Um8c+y1R/5zWuLZsNCk2IQNNtKk3hsfLTpwxcun3p7UTE0mcvf4zmlbncHESBAgACBiQsITSbeAgUQIECAAIHyAsMCgCwoyD8iM9dGpGX2L4lVFY+baTXHti99bfDWnWFhwLCxssd8spUlwzZvjW/+edev/9qMb+aZ7e05+VUrw4KU/Maz33v0ibBh446pVSPZdX+477mhG8FmoUn+rT3ZGNnjOXP5l++4IwkQIECAAIFJCghNJqlvbAIECBAgMKLAsNBk2Jtw4mXLvHJ41I1g43UP5fXAxXNu+C+XhVtu/0bI3v5T3Hsk7mWSvQ45e61ykWqm0CQelz3uk604mesVwfn9SWL4dMmqD4Y//bO/nvHtOcX5xLAk+8j2RvHK4RFvbocTIECAAIEEBYQmCTZFSQQIECBAgMBkBYbtwzLZioxOgAABAgQITEJAaDIJdWMSIECAAAECyQjkH9U5asERBz2SlEyhCiFAgAABAgQaFxCaNE5uQAIECBAgQCAlgWGPG+U3kk2pVrUQIECAAAECzQoITZr1NhoBAgQIECBAgAABAgQIECDQEgGhSUsapUwCBAgQIECAAAECBAgQIECgWQGhSbPeRiNAgAABAgQIECBAgAABAgRaIiA0aUmjlEmAAAECBAgQIECAAAECBAg0KyA0adbbaAQIECBAgAABAgQIECBAgEBLBIQmLWmUMgkQIECAAAECBAgQIECAAIFmBYQmzXobjQABAgQIECBAgAABAgQIEGiJgNCkJY1SJgECBAgQIECAAAECBAgQINCsgNCkWW+jESBAgAABAgQIECBAgAABAi0REJq0pFHKJECAAAECBAgQIECAAAECBJoVEJo06200AgQIECBAgAABAgQIECBAoCUCQpOWNEqZBAgQIECAAAECBAgQIECAQLMCQpNmvY1GgAABAgQIECBAgAABAgQItERAaNKSRimTAAECBAgQIECAAAECBAgQaFZAaNKst9EIECBAgAABAgQIECBAgACBlggITVrSKGUSIECAAAECBAgQIECAAAECzQoITZr1NhoBAgQIECBAgAABAgQIECDQEgGhSUsapUwCBAgQIECAAAECBAgQIECgWQGhSbPeRiNAgAABAgQIECBAgAABAgRaIiA0aUmjlEmAAAECBAgQIECAAAECBAg0KyA0adbbaAQIECBAgAABAgQIECBAgEBLBIQmLWmUMgkQIECAAAECBAgQIECAAIFmBYQmzXobjQABAgQIECBAgAABAgQIEGiJgNCkJY1SJgECBAgQIECAAAECBAgQINCsgNCkWW+jESBAgAABAgQIECBAgAABAi0REJq0pFHKJECAAAECBAgQIECAAAECBJoVEJo06200AgQIECBAgAABAgQIECBAoCUCQpOWNEqZBAgQIECAAAECBAgQIECAQLMCQpNmvY1GgAABAgQIECBAgAABAgQItERAaNKSRimTAAECBAgQIECAAAECBAgQaFZAaNKst9EIECBAgAABAgQIECBAgACBlggITVrSKGUSIECAAAECBAgQIECAAAECzQoITZr1NhoBAgQIECBAgAABAgQIECDQEgGhSUsapUwCBAgQIECAAAECBAgQIECgWQGhSbPeRiNAgAABAgQIECBAgAABAgRaIiA0aUmjlEmAAAECBAgQIECAAAECBAg0KyA0adbbaAQIECBAgAABAgQIECBAgEBLBP5/LqFHiu4+WssAAAAASUVORK5CYII=",
      "text/html": [
       "<div>                            <div id=\"a29a30c7-b4fd-489a-8173-b4322a6fa189\" class=\"plotly-graph-div\" style=\"height:525px; width:100%;\"></div>            <script type=\"text/javascript\">                require([\"plotly\"], function(Plotly) {                    window.PLOTLYENV=window.PLOTLYENV || {};                                    if (document.getElementById(\"a29a30c7-b4fd-489a-8173-b4322a6fa189\")) {                    Plotly.newPlot(                        \"a29a30c7-b4fd-489a-8173-b4322a6fa189\",                        [{\"alignmentgroup\":\"True\",\"hovertemplate\":\"Nome da Regi\\u00e3o=%{x}\\u003cbr\\u003eN\\u00famero de Habitantes=%{y}\\u003cextra\\u003e\\u003c\\u002fextra\\u003e\",\"legendgroup\":\"\",\"marker\":{\"color\":\"#636efa\",\"pattern\":{\"shape\":\"\"}},\"name\":\"\",\"offsetgroup\":\"\",\"orientation\":\"v\",\"showlegend\":false,\"textposition\":\"auto\",\"x\":[\"Centro-Oeste\",\"Nordeste\",\"Norte\",\"Sudeste\",\"Sul\"],\"xaxis\":\"x\",\"y\":[16289538,54658515,17354884,84840113,29937706],\"yaxis\":\"y\",\"type\":\"bar\"}],                        {\"template\":{\"data\":{\"histogram2dcontour\":[{\"type\":\"histogram2dcontour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"choropleth\":[{\"type\":\"choropleth\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"histogram2d\":[{\"type\":\"histogram2d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmap\":[{\"type\":\"heatmap\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"heatmapgl\":[{\"type\":\"heatmapgl\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"contourcarpet\":[{\"type\":\"contourcarpet\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"contour\":[{\"type\":\"contour\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"surface\":[{\"type\":\"surface\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"},\"colorscale\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]]}],\"mesh3d\":[{\"type\":\"mesh3d\",\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}],\"scatter\":[{\"fillpattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2},\"type\":\"scatter\"}],\"parcoords\":[{\"type\":\"parcoords\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolargl\":[{\"type\":\"scatterpolargl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"bar\":[{\"error_x\":{\"color\":\"#2a3f5f\"},\"error_y\":{\"color\":\"#2a3f5f\"},\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"bar\"}],\"scattergeo\":[{\"type\":\"scattergeo\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterpolar\":[{\"type\":\"scatterpolar\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"histogram\":[{\"marker\":{\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"histogram\"}],\"scattergl\":[{\"type\":\"scattergl\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatter3d\":[{\"type\":\"scatter3d\",\"line\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattermapbox\":[{\"type\":\"scattermapbox\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scatterternary\":[{\"type\":\"scatterternary\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"scattercarpet\":[{\"type\":\"scattercarpet\",\"marker\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}}}],\"carpet\":[{\"aaxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"baxis\":{\"endlinecolor\":\"#2a3f5f\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"minorgridcolor\":\"white\",\"startlinecolor\":\"#2a3f5f\"},\"type\":\"carpet\"}],\"table\":[{\"cells\":{\"fill\":{\"color\":\"#EBF0F8\"},\"line\":{\"color\":\"white\"}},\"header\":{\"fill\":{\"color\":\"#C8D4E3\"},\"line\":{\"color\":\"white\"}},\"type\":\"table\"}],\"barpolar\":[{\"marker\":{\"line\":{\"color\":\"#E5ECF6\",\"width\":0.5},\"pattern\":{\"fillmode\":\"overlay\",\"size\":10,\"solidity\":0.2}},\"type\":\"barpolar\"}],\"pie\":[{\"automargin\":true,\"type\":\"pie\"}]},\"layout\":{\"autotypenumbers\":\"strict\",\"colorway\":[\"#636efa\",\"#EF553B\",\"#00cc96\",\"#ab63fa\",\"#FFA15A\",\"#19d3f3\",\"#FF6692\",\"#B6E880\",\"#FF97FF\",\"#FECB52\"],\"font\":{\"color\":\"#2a3f5f\"},\"hovermode\":\"closest\",\"hoverlabel\":{\"align\":\"left\"},\"paper_bgcolor\":\"white\",\"plot_bgcolor\":\"#E5ECF6\",\"polar\":{\"bgcolor\":\"#E5ECF6\",\"angularaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"radialaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"ternary\":{\"bgcolor\":\"#E5ECF6\",\"aaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"baxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"},\"caxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\"}},\"coloraxis\":{\"colorbar\":{\"outlinewidth\":0,\"ticks\":\"\"}},\"colorscale\":{\"sequential\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"sequentialminus\":[[0.0,\"#0d0887\"],[0.1111111111111111,\"#46039f\"],[0.2222222222222222,\"#7201a8\"],[0.3333333333333333,\"#9c179e\"],[0.4444444444444444,\"#bd3786\"],[0.5555555555555556,\"#d8576b\"],[0.6666666666666666,\"#ed7953\"],[0.7777777777777778,\"#fb9f3a\"],[0.8888888888888888,\"#fdca26\"],[1.0,\"#f0f921\"]],\"diverging\":[[0,\"#8e0152\"],[0.1,\"#c51b7d\"],[0.2,\"#de77ae\"],[0.3,\"#f1b6da\"],[0.4,\"#fde0ef\"],[0.5,\"#f7f7f7\"],[0.6,\"#e6f5d0\"],[0.7,\"#b8e186\"],[0.8,\"#7fbc41\"],[0.9,\"#4d9221\"],[1,\"#276419\"]]},\"xaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"yaxis\":{\"gridcolor\":\"white\",\"linecolor\":\"white\",\"ticks\":\"\",\"title\":{\"standoff\":15},\"zerolinecolor\":\"white\",\"automargin\":true,\"zerolinewidth\":2},\"scene\":{\"xaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"yaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2},\"zaxis\":{\"backgroundcolor\":\"#E5ECF6\",\"gridcolor\":\"white\",\"linecolor\":\"white\",\"showbackground\":true,\"ticks\":\"\",\"zerolinecolor\":\"white\",\"gridwidth\":2}},\"shapedefaults\":{\"line\":{\"color\":\"#2a3f5f\"}},\"annotationdefaults\":{\"arrowcolor\":\"#2a3f5f\",\"arrowhead\":0,\"arrowwidth\":1},\"geo\":{\"bgcolor\":\"white\",\"landcolor\":\"#E5ECF6\",\"subunitcolor\":\"white\",\"showland\":true,\"showlakes\":true,\"lakecolor\":\"white\"},\"title\":{\"x\":0.05},\"mapbox\":{\"style\":\"light\"}}},\"xaxis\":{\"anchor\":\"y\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"Nome da Regi\\u00e3o\"}},\"yaxis\":{\"anchor\":\"x\",\"domain\":[0.0,1.0],\"title\":{\"text\":\"N\\u00famero de Habitantes\"}},\"legend\":{\"tracegroupgap\":0},\"title\":{\"text\":\"Popula\\u00e7\\u00e3o por Regi\\u00e3o\"},\"barmode\":\"relative\"},                        {\"responsive\": true}                    ).then(function(){\n",
       "                            \n",
       "var gd = document.getElementById('a29a30c7-b4fd-489a-8173-b4322a6fa189');\n",
       "var x = new MutationObserver(function (mutations, observer) {{\n",
       "        var display = window.getComputedStyle(gd).display;\n",
       "        if (!display || display === 'none') {{\n",
       "            console.log([gd, 'removed!']);\n",
       "            Plotly.purge(gd);\n",
       "            observer.disconnect();\n",
       "        }}\n",
       "}});\n",
       "\n",
       "// Listen for the removal of the full notebook cells\n",
       "var notebookContainer = gd.closest('#notebook-container');\n",
       "if (notebookContainer) {{\n",
       "    x.observe(notebookContainer, {childList: true});\n",
       "}}\n",
       "\n",
       "// Listen for the clearing of the current output cell\n",
       "var outputEl = gd.closest('.output');\n",
       "if (outputEl) {{\n",
       "    x.observe(outputEl, {childList: true});\n",
       "}}\n",
       "\n",
       "                        })                };                });            </script>        </div>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "\n",
    "populacao_por_regiao = view_populacao.groupby('nome_regiao')['numero_habitantes'].sum().reset_index()\n",
    "\n",
    "fig_regiao = px.bar(populacao_por_regiao,\n",
    "                    x='nome_regiao',\n",
    "                    y='numero_habitantes',\n",
    "                    labels={'nome_regiao': 'Nome da Região', 'numero_habitantes': 'Número de Habitantes'},\n",
    "                    title='População por Região')\n",
    "fig_regiao.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "colab": {
   "provenance": []
  },
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
