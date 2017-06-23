using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using MandelbrotSet.Interfaces;
using MandelbrotSet.MainController;

namespace MandelbrotSet
{
    public partial class Main : Form, IMainView
    {
        private Bitmap image;
        private MainController.MainController controller;
        
        public Bitmap Image
        {
            get
            {
                return image;
            }
        }

        public Main()
        {            
            InitializeComponent();
            this.renderButton.Select();
            controller = new MainController.MainController(this);
        }

        private void RenderButtonClick(object sender, EventArgs e)
        {
            if (RenderButtonClicked != null)
            {
                RenderButtonClicked(sender, e);
            }
        }

        private void ClearButtonClick(object sender, EventArgs e)
        {
            if (ClearButtonClicked != null)
            {
                ClearButtonClicked(sender, e);
            }
        }

        private void CloseButtonClick(object sender, EventArgs e)
        {
            if (CloseButtonClicked != null)
            {
                CloseButtonClicked(sender, e);
            }
        }

        private void TopButtonClick(object sender, EventArgs e)
        {
            if (TopButtonClicked != null)
            {
                TopButtonClicked(sender, e);
            }
        }

        private void BottomButtonClick(object sender, EventArgs e)
        {
            if (BottomButtonClicked != null)
            {
                BottomButtonClicked(sender, e);
            }
        }

        private void LeftButtonClick(object sender, EventArgs e)
        {
            if (LeftButtonClicked != null)
            {
                LeftButtonClicked(sender, e);
            }
        }

        private void RightButtonClick(object sender, EventArgs e)
        {
            if (RightButtonClicked != null)
            {
                RightButtonClicked(sender, e);
            }
        }

        private void ZoomValueChange(object sender, EventArgs e)
        {
            if (ZoomValueChanged != null)
            {
                ZoomValueChanged(sender, e);
            }
        }

        private void IterationsInputValueChanged(object sender, EventArgs e)
        {            
            if (IterationsValueChanged != null)
            {
                IterationsValueChanged(sender, e);
            }
        }

        public event EventHandler RenderButtonClicked;
        public event EventHandler ClearButtonClicked;
        public event EventHandler CloseButtonClicked;
        public event EventHandler TopButtonClicked;
        public event EventHandler BottomButtonClicked;
        public event EventHandler LeftButtonClicked;
        public event EventHandler RightButtonClicked;
        public event EventHandler ZoomValueChanged;
        public event EventHandler IterationsValueChanged;

        public void ClearCanvas()
        {
            Size size = new Size(FractalCanvas.Width, FractalCanvas.Height);
            this.image = new Bitmap(size.Width, size.Height);
            FractalCanvas.Image = image;
        }

        public double GetZoom()
        {
            try
            {
                return double.Parse(this.inputZoom.Text);
            }
            catch
            {
                return 100;
            }
        }

        public void Refresh()
        {
            FractalCanvas.Image = image;
        }

        public Bitmap Canvas
        {
            get { return this.image; }
        }

        public int Iterations
        {
            get
            {
                try
                {
                    return Convert.ToInt32(this.iterationsInput.Text);
                }
                catch
                {
                    return 0;
                }
            }
        }

        private void iterationsInput_Scroll(object sender, EventArgs e)
        {

        }

        private void iterationsInput_TextChanged(object sender, EventArgs e)
        {
            if (IterationsValueChanged != null)
            {
                IterationsValueChanged(sender, e);
            }
        }

        private void Main_Load(object sender, EventArgs e)
        {

        }
    }
}
