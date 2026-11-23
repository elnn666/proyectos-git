import sqlite3
import pandas as pd
import streamlit as st

st.title("Centinela")
st.write("Analizador de intentos de acceso SSH")

conexion = sqlite3.connect("salida/centinela.db")

tabla = pd.read_sql_query("""
SELECT ip,
       SUM(CASE WHEN resultado = 'Failed' THEN 1 ELSE 0 END) AS fallidos,
       SUM(CASE WHEN resultado = 'Accepted' THEN 1 ELSE 0 END) AS correctos
FROM intentos
GROUP BY ip
ORDER BY fallidos DESC
""",conexion)

conexion.close()

st.subheader("Intentos de acceso por IP")
st.dataframe(tabla)

st.subheader("Fallidos por IP")
st.bar_chart(tabla, x="ip", y="fallidos")