# Projet Automated Pick and Place avec Bras Robotique et Vision

## Description

Ce projet ROS permet de contrôler un bras robotique (UR5) pour réaliser une tâche de pick-and-place automatisée en utilisant la vision par ordinateur. Le système détecte un objet rouge dans la scène via une caméra simulée, puis commande le bras robotisé pour saisir cet objet et le déplacer.

### Fonctionnalités

- Détection d’objet coloré (rouge) via OpenCV sur flux vidéo ROS.
- Pilotage du bras robotisé UR5 avec MoveIt pour planification et exécution de trajectoires.
- Simulation complète dans Gazebo avec environnement incluant table et objet.
- Architecture modulaire ROS avec nodes séparés pour vision et contrôle du bras.
- Fichier de lancement global pour faciliter le démarrage du système.

---

## Prérequis

- ROS Noetic (ou compatible)
- MoveIt installé et configuré
- Gazebo simulation
- Python 3 avec `cv_bridge`, `rospy`, `moveit_commander`, `opencv-python`
- Paquets ROS standards : `sensor_msgs`, `geometry_msgs`, `robot_state_publisher`, `joint_state_publisher_gui`

---

## Installation

1. Cloner ce dépôt dans le dossier `src` de votre workspace ROS :

```bash
cd ~/catkin_ws/src
git clone <url_du_projet>
```

2. Compiler le workspace :

```bash
cd ~/catkin_ws
catkin_make
source devel/setup.bash
```

3. Installer les dépendances Python si nécessaire :

```bash
pip3 install opencv-python
```

---

## Utilisation 

```bash
roslaunch automated_pick_place demo.launch
```

Le système lance Gazebo, RViz, les noeuds de vision et de contrôle du bras.
La détection d’objet et la manipulation s’effectuent automatiquement.

---

## Architecture du projet

```bash
automated_pick_place/
├── scripts/
│   ├── vision_node.py          # Détection d’objet rouge avec OpenCV
│   └── pick_place_controller.py # Commande MoveIt du bras UR5
├── launch/
│   └── demo.launch             # Lancement complet du système
├── urdf/
│   └── ur5.urdf.xacro          # Modèle UR5
├── worlds/
│   └── table_scene.world       # Monde Gazebo avec table et objet
├── config/
│   └── moveit_config/          # Configuration MoveIt générée
```

---

## Contrôle du bras

- Le bras est contrôlé via MoveIt à partir des coordonnées détectées de l’objet.
- Le noeud pick_place_controller.py écoute la position détectée et génère une trajectoire de prise puis déplacement.

---

## Notes 

- Le système est basé sur un modèle simulé. Pour une utilisation réelle, adapter le modèle URDF et la source vidéo.
- La détection d’objet est simple (seuil HSV) et peut être améliorée avec des méthodes plus avancées.
- La sécurité et la robustesse ne sont pas couvertes, à ajouter selon besoins industriels.
