# =============================================================================
# STREAMLIT APP: Calculadora de Clasificación para Coriorretinopatía Serosa Central (CSC)
# =============================================================================
# Creada por el Dr. Luis Daniel García Arzate (letra pequeña)
#
# Este ejemplo ilustra cómo asignar valores a cada uno de los ejes T-A-E-R y
# mostrar un código de clasificación final junto con recomendaciones generales.

import streamlit as st

def main():
    # Configuración de la página
    st.set_page_config(
        page_title="IC-CSC Calculator",
        layout="centered"
    )
    
    # Encabezado principal
    st.title("Calculadora IC-CSC")
    st.caption("Creada por el Dr. Luis Daniel García Arzate")
    st.write("""
        ### International Classification for Central Serous Chorioretinopathy (IC-CSC)
        Seleccione los valores correspondientes a cada eje:
        - **T (Temporal)**: T0, T1, T2
        - **A (Activity)**: A0, A1, A2
        - **E (Extension)**: E0, E1, E2
        - **R (Risk)**    : R0, R1, R2
    """)

    # Selección de valores para cada eje
    t_value = st.selectbox(
        "Temporal (T)",
        options=["T0 (Acute)", "T1 (Recurrent)", "T2 (Chronic)"],
        index=0
    )
    a_value = st.selectbox(
        "Activity (A)",
        options=["A0 (Inactive)", "A1 (Mild/Moderate)", "A2 (Severe)"],
        index=0
    )
    e_value = st.selectbox(
        "Extension (E)",
        options=["E0 (Focal)", "E1 (Multifocal/Diffuse)", "E2 (Extensive/Chronic Changes)"],
        index=0
    )
    r_value = st.selectbox(
        "Risk (R)",
        options=["R0 (No/Minimal)", "R1 (Moderate)", "R2 (High)"],
        index=0
    )

    # Extraemos solo la sigla T0, T1, etc. (quitando la descripción en paréntesis)
    t_code = t_value.split()[0]
    a_code = a_value.split()[0]
    e_code = e_value.split()[0]
    r_code = r_value.split()[0]

    # Mostramos la clasificación final
    st.markdown("---")
    st.subheader("Clasificación IC-CSC Generada")
    st.write(f"**Código**: {t_code}-{a_code}-{e_code}-{r_code}")

    # Recomendaciones generales en base a la clasificación
    # Se podrían añadir más condiciones/ramas de decisión según la combinación.
    st.markdown("---")
    st.subheader("Recomendaciones Clínicas y Terapéuticas")

    recommendations = []

    # Sugerencias simples por cada eje (a modo de ejemplo)
    if t_code == "T0":
        recommendations.append("- Manejo conservador (observación) si la AV es adecuada.")
    elif t_code == "T1":
        recommendations.append("- Monitorizar más de cerca; evaluar riesgos de recidiva.")
    else:  # T2
        recommendations.append("- Considerar terapias activas como fotodinámica o láser micropulsado.")

    if a_code == "A2":
        recommendations.append("- Alta prioridad de intervención para evitar secuelas visuales.")
    elif a_code == "A1":
        recommendations.append("- Seguimiento con OCT; posible tratamiento focal si la visión está afectada.")

    if e_code == "E2":
        recommendations.append("- Cambios crónicos en EPR: mayor riesgo de secuelas permanentes.")
    elif e_code == "E1":
        recommendations.append("- Lesiones multifocales: vigilar posible confluencia de fluido.")

    if r_code == "R2":
        recommendations.append("- Ajustar factores sistémicos: disminuir esteroides, control estricto del estrés.")
    elif r_code == "R1":
        recommendations.append("- Identificar factores modificables (ansiedad, obesidad, HT leve).")

    # Mostramos las recomendaciones
    if recommendations:
        for rec in recommendations:
            st.write(rec)
    else:
        st.write("Sin recomendaciones específicas adicionales.")

    st.markdown("---")
    st.write("""
        **Nota**: Esta calculadora es un ejemplo educativo; el manejo real de cada paciente 
        debe basarse en una evaluación clínica completa, la experiencia del oftalmólogo y 
        las guías más actualizadas.
    """)

if __name__ == "__main__":
    main()
