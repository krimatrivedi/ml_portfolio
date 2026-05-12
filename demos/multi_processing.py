import streamlit as st
import multiprocessing
import time
import random


def agent(name, q):
    missions = [
        "🔍 Scanning secret files",
        "🧪 Running experiments",
        "📊 Analyzing datasets",
        "⚙️ Optimizing code",
        "🚀 Preparing results"
    ]

    for step, mission in enumerate(missions, start=1):
        time.sleep(random.uniform(0.7, 1.4))
        q.put(f"{name}: {mission}... (step {step}/5)")

    q.put(f"{name}: 🎉 Mission Complete!")


def run_demo():
    st.set_page_config(page_title="Multiprocessing Story Demo", page_icon="🤖")
    st.title("🤖 Parallel Agents Demo – How Multiprocessing Actually Runs Behind the Scenes")

    if "logs" not in st.session_state:
        st.session_state.logs = []

    st.markdown("""
    Welcome to the **Python Secret Agency** 🕵️‍♂️  
    Watch how two agents run **in true parallel**, sending updates live from separate CPU cores!
    """)

    if st.button("🚀 Launch Parallel Missions"):
        multiprocessing.set_start_method("spawn", force=True)
        print("+++++++1+++++++++++++++++++")

        q = multiprocessing.Queue()
        print("+++++++1+++++++++++++++++2++")

        agent_a = multiprocessing.Process(target=agent, args=("🕵️ Agent A", q))
        print("+++++++1+++++++++++++++++3++")
        agent_b = multiprocessing.Process(target=agent, args=("🕵️ Agent B", q))
        print("+++++++1+++++++++++++++++4++")

        agent_a.start()
        print("+++++++1+++++++++++++++++5++")
        agent_b.start()
        print("+++++++1+++++++++++++++++6++")

        st.subheader("📡 Live Mission Feed")
        output_box = st.empty()

        # 🔥 LIVE UPDATE LOOP
        while agent_a.is_alive() or agent_b.is_alive() or not q.empty():
            try:
                msg = q.get_nowait()
                st.session_state.logs.append(msg)
            except:
                pass

            # Update UI
            output_box.markdown("\n".join(st.session_state.logs))

            time.sleep(0.1)  # smooth refresh rate

        agent_a.join()
        agent_b.join()

        st.success("🎯 Both missions completed in parallel!")


if __name__ == "__main__":
    run_demo()
