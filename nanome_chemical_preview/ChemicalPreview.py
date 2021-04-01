import nanome

from rdkit import Chem
from rdkit.Chem import AllChem, Draw

import tempfile
import shutil
from cairosvg import svg2png

# mol 2d image drawing options
Draw.DrawingOptions.atomLabelFontSize = 40
Draw.DrawingOptions.dotsPerAngstrom = 100
Draw.DrawingOptions.bondLineWidth = 8

class ChemicalPreview(nanome.PluginInstance):
    def start(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.temp_sdf = tempfile.NamedTemporaryFile(delete=False, suffix='.sdf', dir=self.temp_dir.name)
        self.integration.generate_molecule_image = self.generate_images

    def generate_images(self, request):
        ligand_list, resolution = request.get_args()
        images = [self.generate_image(ligand, resolution) for ligand in ligand_list]
        request.send_response(images)

    def generate_image(self, complex, resolution):
        complex.io.to_sdf(self.temp_sdf.name)
        try:
            mol = Chem.SDMolSupplier(self.temp_sdf.name)[0]
        except Exception as e:
            return ''

        if mol is None:
            return ''

        Chem.AssignStereochemistryFrom3D(mol)
        AllChem.Compute2DCoords(mol)
        mol = Draw.rdMolDraw2D.PrepareMolForDrawing(mol)

        width, height = resolution
        drawer = Draw.rdMolDraw2D.MolDraw2DSVG(width, height)
        drawer.drawOptions().additionalAtomLabelPadding = 0.3
        drawer.DrawMolecule(mol)
        drawer.FinishDrawing()
        svg = drawer.GetDrawingText()
        svg = svg.replace('stroke-linecap:butt', 'stroke-linecap:round')

        path = tempfile.NamedTemporaryFile(delete=False, suffix='.png', dir=self.temp_dir.name).name
        svg2png(bytestring=svg, write_to=path, output_width=width, output_height=height)

        with open(path, 'rb') as f:
            image = f.read()

        return image

def main():
    plugin = nanome.Plugin('2D Chemical Preview', 'A Nanome Plugin to generate 2D images of molecules using RDKit', 'Molecule Image', False)
    plugin.set_plugin_class(ChemicalPreview)
    plugin.run()

if __name__ == '__main__':
    main()
