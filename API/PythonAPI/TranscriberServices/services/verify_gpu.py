import torch

def check_torch_cuda():
  print("🔍 Checking PyTorch CUDA environment...\n")

  print(f"PyTorch version: {torch.__version__}")
  print(f"CUDA available : {torch.cuda.is_available()}")

  if torch.cuda.is_available():
    print(f"Device count   : {torch.cuda.device_count()}")
    for i in range(torch.cuda.device_count()):
      print(f" - GPU {i}: {torch.cuda.get_device_name(i)}")
    print(f"Current device : {torch.cuda.current_device()}")
  else:
    print("CUDA is not available. You might be running on CPU.")

if __name__ == "__main__":
  check_torch_cuda()
