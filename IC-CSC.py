# =============================================================================
# STREAMLIT APP: Calculadora de Clasificación para Coriorretinopatía Serosa Central (CSC)
# =============================================================================
# Creada por el Dr. Luis Daniel García Arzate (letra pequeña)
#
# Referencias Principales:
# 1. Nicholson B, Noble J, Forooghian F, Meyerle C. Central serous chorioretinopathy:
#    update on pathophysiology and treatment. Surv Ophthalmol. 2013;58(5):357–365.
# 2. Wang M, Munch IC, Hasler PW, Prunte C, Larsen M. Central serous chorioretinopathy.
#    Acta Ophthalmol. 2008;86(2):126–145.
# 3. Yannuzzi LA. Central serous chorioretinopathy: a personal perspective. Am J Ophthalmol.
#    2010;149(3):361–363.
# 4. Tsai DC, Chen SJ, Huang CC, Chou P, Lin TH. Epidemiology of central serous chorioretinopathy
#    in Taiwan, 2001–2006: a population-based study. PLoS ONE. 2013;8(6):e66858.
# 5. Spaide RF, Hall L, Haas A, et al. Indocyanine green videoangiography of older patients
#    with central serous chorioretinopathy. Retina. 1996;16(3):203–213.
#
# Este ejemplo ilustra cómo asignar valores a cada uno de los ejes T-A-E-R y
# mostrar un código de clasificación final junto con explicaciones adicionales
# para oftalmólogos que deseen mayor orientación acerca de cada estadio.

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
        ---
        **Objetivo:** Proveer un sistema estandarizado que describa de forma integral
        la Coriorretinopatía Serosa Central, basado en:
        
        - **T (Temporal)**: T0, T1, T2
        - **A (Activity)**: A0, A1, A2
        - **E (Extension/Morphology)**: E0, E1, E2
        - **R (Risk factors)**: R0, R1, R2

        El código final **IC-CSC** se compone de estos cuatro ejes y sirve para
        guiar la toma de decisiones clínicas e impulsar la investigación de la CSC.
    """)

    with st.expander("Ver detalles de la Clasificación (T, A, E, R)"):
        st.markdown("""
        **T (Temporal)**  
        - **T0 (Aguda):** Episodio reciente de CSC con <3 meses de evolución. Usualmente, muchos casos agudos se resuelven de manera espontánea.  
        - **T1 (Recurrente):** Al menos un episodio previo de CSC documentado. La presencia de episodios repetidos puede asociarse a mayor riesgo de complicaciones.  
        - **T2 (Crónica):** Duración >3–6 meses. Suele haber alteraciones en el epitelio pigmentario (EPR) y mayor probabilidad de secuelas visuales.

        **A (Actividad)**  
        - **A0 (Inactiva):** Sin fluido subretiniano significativo en OCT o mínimo y estable, con agudeza visual estable.  
        - **A1 (Leve/Moderada):** Presencia de fluido subretiniano discreto y/o fugas focales en angiografía; afectación visual leve o moderada.  
        - **A2 (Severa):** Extensas áreas de fluido subretiniano, múltiples fugas angiográficas o patrón difuso; la agudeza visual puede estar comprometida de manera notable.

        **E (Extensión/Morfología)**  
        - **E0 (Focal):** Área pequeña de desprendimiento seroso, generalmente <1–2 diámetros de papila, con fugas bien delimitadas.  
        - **E1 (Multifocal/Difusa):** Varias áreas de fluido subretiniano que pueden confluir; fugas múltiples.  
        - **E2 (Extensas/Cambios Crónicos):** Cambios a largo plazo en el EPR, posible fibrosis subretiniana, atrofia o “tracks” gravitacionales.

        **R (Factores de Riesgo)**  
        - **R0 (Mínimo/Nulo):** Sin uso de esteroides o condiciones sistémicas asociadas (ej. estrés crónico severo).  
        - **R1 (Moderado):** Uso esporádico de esteroides (inhalados, tópicos), hipertensión leve, estrés moderado o ansiedad.  
        - **R2 (Alto):** Uso crónico de esteroides sistémicos, trastornos endocrinos (ej. Cushing), estrés crónico severo o comorbilidades importantes.
        
        ---
        **Interpretación General**  
        - Un caso **T0-A0-E0-R0** indicaría CSC aguda, sin actividad aparente, pequeña extensión y sin factores de riesgo importantes: manejo conservador.  
        - Un caso **T2-A2-E2-R2** implicaría CSC crónica, altamente activa, con cambios morfológicos extensos y factores de riesgo sistémicos significativos: demandando intervención activa (láser micropulsado, fotodinámica, modificación de factores de riesgo).
        """)

    # Selección de valores para cada eje
    st.subheader("Seleccione los valores para cada eje")
    t_value = st.selectbox(
        "Temporal (T)",
        options=["T0 (Aguda, <3 meses)", "T1 (Recurrente)", "T2 (Crónica, >3–6 meses)"],
        index=0
    )
    a_value = st.selectbox(
        "Actividad (A)",
        options=["A0 (Inactiva)", "A1 (Leve/Moderada)", "A2 (Severa)"],
        index=0
    )
    e_value = st.selectbox(
        "Extensión/Morfología (E)",
        options=["E0 (Focal)", "E1 (Multifocal/Difusa)", "E2 (Extensa/Cambios crónicos)"],
        index=0
    )
    r_value = st.selectbox(
        "Factores de Riesgo (R)",
        options=["R0 (Mínimo o nulo)", "R1 (Moderado)", "R2 (Alto)"],
        index=0
    )

    # Extraemos solo la "sigla" de cada selección (e.g. "T0", "A1", etc.)
    t_code = t_value.split()[0]
    a_code = a_value.split()[0]
    e_code = e_value.split()[0]
    r_code = r_value.split()[0]

    # Sección de resultados
    st.markdown("---")
    st.subheader("Clasificación IC-CSC Generada")
    st.write(f"**Código:** {t_code}-{a_code}-{e_code}-{r_code}")

    st.markdown("---")
    st.subheader("Recomendaciones Clínicas y Terapéuticas")

    # Lógica básica de recomendaciones
    recommendations = []

    # Temporal (T)
    if t_code == "T0":
        recommendations.append("- La CSC aguda puede resolverse espontáneamente; se sugiere observación inicial si la AV es adecuada.")
    elif t_code == "T1":
        recommendations.append("- Se debe vigilar la aparición de nuevos episodios; valorar terapia si hay deterioro visual significativo.")
    else:  # T2
        recommendations.append("- La CSC crónica conlleva mayor riesgo de secuelas; considerar PDT (fotodinámica) o láser micropulsado, según el caso.")

    # Actividad (A)
    if a_code == "A2":
        recommendations.append("- Priorizar tratamiento para reducir el riesgo de secuelas visuales (fotodinámica dosis baja, láser micropulsado, etc.).")
    elif a_code == "A1":
        recommendations.append("- Seguimiento con OCT para confirmar estabilidad; considerar tratamiento focal según afectación de la visión.")
    else:  # A0
        recommendations.append("- Actividad inactiva: observación o manejo conservador, salvo factores especiales.")

    # Extensión (E)
    if e_code == "E2":
        recommendations.append("- Cambios crónicos del EPR (atrofia, fibrosis); la recuperación visual puede ser limitada. Requiere seguimiento continuo.")
    elif e_code == "E1":
        recommendations.append("- Lesiones multifocales o difusas: riesgo mayor de recurrencia; control con angiografía o OCT multimodal.")
    else:  # E0
        recommendations.append("- Lesión focal: generalmente mejor pronóstico espontáneo.")

    # Riesgo (R)
    if r_code == "R2":
        recommendations.append("- Ajustar factores sistémicos (p.ej., reducir esteroides si es posible, manejo intensivo del estrés).")
    elif r_code == "R1":
        recommendations.append("- Identificar y controlar factores predisponentes (HT leve, uso esporádico de esteroides, estrés moderado).")
    else:  # R0
        recommendations.append("- Sin factores de riesgo mayores identificados: mantener control periódico y educación al paciente.")

    # Mostrar recomendaciones finales
    if recommendations:
        st.write("**Sugerencias de manejo:**")
        for rec in recommendations:
            st.write(rec)
    else:
        st.write("Sin recomendaciones específicas adicionales.")

    st.markdown("---")
    st.write("""
    **Nota**: Esta calculadora es de carácter ilustrativo; el manejo real de cada caso
    debe basarse en la evaluación clínica integral, la experiencia del oftalmólogo y 
    las guías más actualizadas.

    ---
    **Referencias**:
    1. Nicholson B, Noble J, Forooghian F, Meyerle C. Central serous chorioretinopathy: update on pathophysiology and treatment. *Surv Ophthalmol.* 2013;58(5):357–365.  
    2. Wang M, Munch IC, Hasler PW, Prunte C, Larsen M. Central serous chorioretinopathy. *Acta Ophthalmol.* 2008;86(2):126–145.  
    3. Yannuzzi LA. Central serous chorioretinopathy: a personal perspective. *Am J Ophthalmol.* 2010;149(3):361–363.  
    4. Tsai DC, Chen SJ, Huang CC, Chou P, Lin TH. Epidemiology of central serous chorioretinopathy in Taiwan, 2001–2006: a population-based study. *PLoS ONE.* 2013;8(6):e66858.  
    5. Spaide RF, Hall L, Haas A, et al. Indocyanine green videoangiography of older patients with central serous chorioretinopathy. *Retina.* 1996;16(3):203–213.
    """)

if __name__ == "__main__":
    main()
