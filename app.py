# ---- GENERATE STORY (Placeholder) ----
st.markdown("---")
st.subheader("📖 Your Generated Story")

generated_story = ""

if st.button("Generate"):
    st.success("✨ Story Generated!")
    generated_story = f"""
**Title:** *{genre} Chronicles: The Rise of {protagonist}*

In a world where stardust veins pulse through machines and forgotten ruins orbit black suns, **{protagonist}** awakens in a derelict satellite. Humanity’s last hope, equipped with a memory that isn’t theirs and a mission older than time.

As cybernetic storms brew over the neon rings of Jupiter, whispers of rebellion echo through the void...

*(The rest of your galactic tale continues...)*  
"""
    st.markdown(generated_story)

    # Save story to downloadable text file
    story_file = f"{protagonist}_scifi_story.txt"
    st.download_button(
        label="💾 Save Story as .txt",
        data=generated_story,
        file_name=story_file,
        mime="text/plain"
    )
else:
    st.warning("⬅️ Fill in the details and click Generate")
