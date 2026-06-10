---
id: c01d835b44
question: 'GCP VM: If you have lost SSH access to your machine due to lack of space.
  Permission denied (publickey)'
sort_order: 23
---

If your VM's boot disk is full you can lose SSH access. To recover, create a bigger boot disk from a snapshot of the old one and start a new instance from it:

1. In the Google Cloud console, go to the **VM instances** page.
   - Click the instance name to open the **VM instance details** page.
   - Click **Stop**.
   - In the **Boot disk** section, note the boot disk's size and name.
2. In the Google Cloud console, go to the **Create a snapshot** page.
   - Enter a snapshot **Name**.
   - Select the boot disk from the **Source disk** drop-down list.
   - Click **Create**.
3. In the Google Cloud console, go to the **Create an instance** page.
4. Enter the instance details.
5. Create a new boot disk from the snapshot of the old boot disk:
   - Under **Boot disk**, select **Change**.
   - Select **Snapshots**.
   - Select the snapshot of the old boot disk from the **Snapshot** drop-down list.
   - Select the **Boot disk type**.
   - Enter the new size for the disk (larger than before, so you don't run out of space again).
   - Click **Select** to confirm your disk options.
6. Click **Create**.
