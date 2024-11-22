import sys
from PyQt5.QtWidgets import QApplication

from visualization import InversionModelPredictDialog

app = QApplication(sys.argv)
edge_infor_path = r"./edge_info/edge_info_data_enhance.json"
inversion_detection_model_path = r"./model/D_R/40000"
inversion_model_training_dict = {"TF_use_edge_q":True,
                                            "TF_use_edge_p":True,
                                            "TF_use_node_q":True,
                                            "TF_use_node_p":True}  # Define appropriately
sensors_location_set_dict = {
                            "sensor_all_location" : False,  
                            "sensor_true_location" : True,
                            "sensor_input_location" : False,
                            "input_sensors_infor_dict" : {}
                            } # Define appropriately
imagePath = r"./network/network_data_enhance.png"
main_window = InversionModelPredictDialog(edge_infor_path, inversion_detection_model_path,
                                            inversion_model_training_dict, sensors_location_set_dict, imagePath)
main_window.show()
sys.exit(app.exec_())